
var API_URL = window.location.href;

function makePostRequest(url, data, onSuccess, onFailure) {
    $.ajax({
        type: 'POST',
        url: API_URL + url,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: onSuccess,
        error: onFailure
    });
}

function getSearchData() {
    name_box = $("input[name=player_name]").val();
    week = $("input[name=week]").val();
    year = $("input[name=year]").val();
    var data = {
        'success': 1,
        'name': name_box,
        'week': parseInt(week),
        'year': parseInt(year)
    };
    return data;
}

function onPlayerSearch() {
    $(".player-submit").on("click", function () {
//        var crap_data = getSearchData();
//        var new_data = JSON.stringify(crap_data);
        name_box = $("input[name=player]").val();
        week = $("input[name=week]").val();
        year = $("input[name=year]").val();
        var crap_data = {
            'success': 1,
            'player_name': name_box,
            'week': parseInt(week),
            'year': parseInt(year)
        };
        var onSuccessFnc = function(data) {
            console.log("SUCCESS");
        };
        var onFailureFnc = function(data) {
            return 'ERRRORROROROROR';
        };
        makePostRequest('stats', crap_data, onSuccessFnc, onFailureFnc);

    })
}

function generateStats() {
    new_html = "<div class='stats'>" + "asdsad" + "</div>";
    return new_html;
}

$(document).ready(function() {
    onPlayerSearch();
});