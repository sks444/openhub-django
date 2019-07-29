$(document).ready(function () {
    let search_input = $('.input-group #search-list');
    let searched_keyword = null;
    let list_items = $('.main-content .collection a');
    if(list_items.length !== 0){
        search_input.on('keypress keyup', function () {
            searched_keyword = search_input.val();
            $('.not-found').remove();
            if(searched_keyword === ''){
                list_items.css('display', 'block');
            }
            else {
                let results = $('[id^=' + searched_keyword +']');
                list_items.css('display', 'none');
                if (results.length !== 0) {
                    results.css('display', 'block');
                }
                else {
                    let not_found_el = '<span class="not-found">' +
                                       'No results found for your search ' +
                                       '<i class="fa fa-frown-o"' +
                                       ' aria-hidden="true"></i></span>';
                    $('.container').append(not_found_el);
                }
            }
        })
    }
    else {
        search_input.attr('disabled', true);
    }

});
