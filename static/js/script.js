$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('select').formSelect();
    $("#copyright").text(new Date().getFullYear());




    if (screen.width < 480) {
        $('.edit-cancel-btn').removeClass('btn-large').addClass('btn-small');
        $('.edit-submit-btn').removeClass('btn-large').addClass('btn-small');
        $('.add-recipe-btn').removeClass('btn-large').addClass('btn-small');
        $('.edit-category-cancel-btn').removeClass('btn-large').addClass('btn-small');
        $('.edit-category-edit-btn').removeClass('btn-large').addClass('btn-small');
    }

    // confirm delete recipe
    $(".del").click(function(){
        var delete_confirmed = confirm("Delete this recipe?");
        if (delete_confirmed){
            window.location.href = "{{ url_for('delete_recipe', recipe_id=recipes._id) }}";
            alert("The recipe has successfully been deleted");
        }else {
            return false;
            alert("The recipe has not benn deleted");
            
        }
    });


    // The code was borrowed from Tim Nelson tutorial
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});