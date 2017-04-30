
$('#close-post').click(function(){
    console.log('clicked');
    $('#top_post').css('display', 'none');
    $('this').hide();
})

$('#searchbar').keyup(function(){
  $('#search_results').children("ul").children('li').remove();
  var query = $('#searchbar').val();
  console.log(query);
  if (query != ''){
    $.ajax({url: "/post_search", data: {'query_string': query}, success: function(result){
          result1 = JSON.parse(result)
          if (result1.length == 0){
            $('#search_results').css('display', 'none');
          }
          $('#search_results').css('display', 'flex');
          for (i = 0; i < result1.length; i++){
            $('#search_results ul').append('<li>Every time I ' + result1[i].fields.trigger + ', I ' + result1[i].fields.habit + '</li>')
          }
    }})};
  if (query == '') {
    $('#search_results').children("ul").children('li').remove();
    $('#search_results').css('display', 'none');
  };
})
