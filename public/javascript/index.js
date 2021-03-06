function query(formData) {
    var url = formData.url;
    var layer = 2;
    var params = '?url=' + url + '&layer=' + layer;
    waitingDialog.show('Generating report', {progressType: 'success'});
    ajax('GET', '/json/query' + params, {}, true, function (response) {
        if (response.error == 0) {
            init_report(response);
            waitingDialog.hide();
        }
        else {
            waitingDialog.hide();
            showNoticeDialog('Failed', 'Query failed!' + response.errorMsg);
        }
    });
}


function append_https(url) {
    if (url.startsWith('http'))
        return url;
    return 'https://' + url;
}

function init_report(response) {
    $('#report-title').text('Safety Report: ' + response.root.url)
    init_graph(response.data);
    init_safety(response.root);

    jump_url = append_https(response.root.url);

    jump_fun = function (event) {
        event.preventDefault();
        window.location.href = jump_url;
    }

    if (response.root.safety >= 75) {
        $('#report-jump').removeAttr('data-toggle');
        $('#report-jump').click(jump_fun);
    }
    else {
        $('#confirm-confirm-btn').click(jump_fun);
    }
    $('#report').modal('show');
}

function componentToHex(c) {
    var hex = c.toString(16)
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function rgbToColorStr(r, g, b) {
    reducedRed = r / 128;
    reducedGreen = g / 128;
    reducedBlue = b / 128;
    reducedColor = reducedBlue + reducedGreen * 2 + reducedRed * 4;
    switch (reducedColor) {
       case 0: return "black"; break;
       case 1: return "blue"; break;
       case 2: return "green"; break;
       case 3: return "cyan"; break;
       case 4: return "red"; break;
       case 5: return "purple"; break;
       case 6: return "yellow"; break;
       case 7: return "white"; break;
    }
    return "black";
}

function get_rgb(min, max, v, str) {
    ratio = 2 * (v - min) / (max - min);
    b = Math.max(0, Math.floor(255 * (1 - ratio)));
    r = Math.max(0, Math.floor(255 * (ratio - 1)));
    g = 255 - b - r;
    if (!str)
        return rgbToHex(r, g, b);
    else
        return rgbToColorStr(r, g, b);
}

function init_safety(root) {
    var target = root.safety;
    if (target >= 75)
        color = 'green'
    else
        color = 'red'

    var percent_number_step = $.animateNumber.numberStepFactories.append(' %')
    $('#report-safety').animateNumber(
      {
        number: target,
        color: color,
        'font-size': '30px',
        easing: 'easeInQuad',
        numberStep: percent_number_step
      },
      15000
    );
}

function init_graph(data) {
    var g = new Springy.Graph();
    var nodes = [];

    for (i = 0; i < data.length; i++) {
        nodes.push(g.newNode({label: data[i].u, color: get_rgb(0, 100, data[i].s)}));
        if (data[i].f != null)
            g.newEdge(nodes[data[i].f], nodes[i], {color: get_rgb(0, 5, data[i].t), label: "" + data[i].t + " times"});
    }

    $(function () {
        var springy = window.springy = $('#report-graph').springy({
            graph: g,
            nodeSelected: function(node) {
                console.log('Node selected: ' + JSON.stringify(node.data));
            }
        });
    });
}

document.getElementById('queryform').onsubmit = function (e) {
    e.preventDefault();
    var formData = $('#queryform').serializeObject();
    query(formData);
    this.reset();
}

