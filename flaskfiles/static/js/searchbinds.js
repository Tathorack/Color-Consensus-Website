$('#search-submit').click(function(){
  search();
});
$('#search-string').bind('keydown', function(e) {
  if (e.keyCode == 13) {
    search();
  }
});
$('#search-string').click(function(){
  $('#search-string').val('');
});
