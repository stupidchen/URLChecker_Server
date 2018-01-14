function query(formData) {
    var url = formData.url;
    var layer = 2;
    var params = '?url=' + url + '&layer=' + layer;
    ajax('GET', '/json/query' + params, {}, true, function (response) {
        if (response.error == 0) {
            init_report(response);
        }
        else {
            showNoticeDialog('Failed', 'Query failed!' + response.errorMsg);
        }
    });
}


function init_report(response) {
    $('#report-url').text('Safety of ' + response.root.url + ': ');
    init_graph(response.data);
    init_safety(response.root);
    $('#report').modal('show');
}

function componentToHex(c) {
    var hex = c.toString(16)
    return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function get_rgb(min, max, v) {
    ratio = 2 * (v - min) / (max - min);
    b = Math.max(0, Math.floor(255 * (1 - ratio)));
    r = Math.max(0, Math.floor(255 * (ratio - 1)));
    g = 255 - b - r;
    return rgbToHex(r, g, b);
}

function init_safety(root) {
    var target = root.safety;
    var color = get_rgb(0, 100, target)

    var percent_number_step = $.animateNumber.numberStepFactories.append(' %')
    $('#report-safety').animateNumber(
      {
        number: target,
        color: color,
        'font-size': '30px',

        easing: 'easeInQuad',

        numberStep: percent_number_step
      },
      'slow'
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

