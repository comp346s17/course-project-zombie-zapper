
$('#close-post').click(function(){
    console.log('clicked');
    $('#top_post').css('display', 'none');
    $('this').hide();
})

$('#searchbar').keyup(function(){
  var query = $('#searchbar').val();
  if (query != ''){
    $.ajax({url: "/post_search", data: {'query_string': query}, success: function(result){
          console.log(result);
          $('#search_results').css('display', 'flex');
          for (i = 0; i < result.length; i++){
            $('#search_results ul').append('<li>Every time I ' + result[i][0] + ', I ' + result[i][1] + '</li>')
          }
    }})};
  if (query == '') {
    $('#search_results').css('display', 'none');
  };
})
