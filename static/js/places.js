$(document).ready(function () {
    shown_places = places;
    console.log(shown_places);
    update_places(shown_places);

    $('.category').on('click', function () {
        $(".selected-category").removeClass("selected-category");
        var cat = $(this).find("h4").text();
        update_places(places, cat);
        $(this).addClass("selected-category");
    });

    function update_places(places, category) {
        var filtered_places = [];
        if (category) {
            for (var i = 0; i < places.length; i++) {
                if (places[i].category == category) {
                    filtered_places.push(places[i]);
                }
            }
        } else {
            filtered_places = places;
        }
        console.log(filtered_places);
        $("#places-container").empty();
        $("#places-map-container").empty();
        for (var i = 0; i < filtered_places.length; i++) {
            var place = filtered_places[i];
            var new_place = "<a href='/place_info/" + place.id + "'><div class='uk-card uk-card-default uk-grid-collapse uk-child-width-1-2@s uk-margin'  uk-grid><div class='uk-card-media-left uk-cover-container'> <img src='" + place.image
                + "' alt='' uk-cover></div><div><div class='uk-card-body'><h3 class='uk-card-title'>" + place.name + "</h3><span class='uk-label uk-label-warning uk-margin-remove uk-padding-remove'>" + place.category + "</span> <p>" + place.description.substring(1, 100) + " ...</p> </div> </div> </div> </a>";
            $("#places-container").append(new_place);

            if (place.x && place.y) {
                var new_point = "<a class='uk-position-absolute uk-transform-center place-on-map uk-icon uk-icon-image place-map' id='place-" + place.id +
                    "' style='left: " + place.x + "%; top: " + place.y + "%; width: 10px;' href='/place_info/" + place.id + "' uk-tooltip='" + place.name + "'></a>"
                $("#places-map-container").append(new_point);
            }
        }
    }

});
