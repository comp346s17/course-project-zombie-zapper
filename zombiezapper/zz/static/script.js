
$('#close-post').click(function(){
    console.log('clicked');
    $('#top_post').css('display', 'none');
    $('this').hide();
})

$('#searchbar').keyup(function(){
  var query = $('#searchbar').val();
  if (query != ''){
    $.ajax({url: "/post_search", data: {'query_string': query}, success: function(result){
          result1 = JSON.parse(result)
          $('#search_results').css('display', 'flex');
          for (i = 0; i < result.length; i++){
            $('#search_results ul').append('<li>Every time I ' + result[i]['trigger'] + ', I ' + result[i]['habit'] + '</li>')
          }
    }})};
  if (query == '') {
    $('#search_results').css('display', 'none');
  };
})
