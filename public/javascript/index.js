function query(formData) {
    var url = formData.url;
    var layer = 1;
    var params = '?url=' + url + '&layer=' + layer;
    ajax('GET', '/json/related' + params, {}, true, function (response) {
        if (response.error == 0) {
            init_graph(response.data);
            $('#result-modal').modal('show');
        }
        else {
            showNoticeDialog('Failed', 'Query failed!' + response.errorMsg);
        }
    });
}

function init_graph(data) {
    var g = new Springy.Graph();
    var nodes = [];

    for (i = 0; i < data.length; i++) {
        nodes.push(g.newNode({label: data[i].u}));
        if (data[i].f != null)
            g.newEdge(nodes[i], nodes[data[i].f]);
    }

    $(function () {
        var springy = window.springy = $('#graph').springy({
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