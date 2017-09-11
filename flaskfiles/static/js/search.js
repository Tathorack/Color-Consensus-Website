var isSubmitting = false;
function search(){
  console.log('search called')
  if(isSubmitting) {
    return;
  }
  var query = $('#search-string').val()
  if(query.length < 1){
    return;
  }
  isSubmitting = true;
  console.log('Submitting')
  var data={
    'search': query,
  }
  console.log(data)
  $.ajax({
    url: $SCRIPT_ROOT + '/search_average/_search_single',  //server script to process data
    type: 'POST',
    headers: {'Content-Type': 'application/json; charset=UTF-8'},
    xhr: function() {
      var xhr = new window.XMLHttpRequest();
      xhr.upload.addEventListener("progress", function(evt) {
        if (evt.lengthComputable) {
          var percentComplete = evt.loaded / evt.total;
            percentComplete = parseInt(percentComplete * 100);
            if (percentComplete === 100) {
              $('#process-progress').removeClass('progress-bar-info');
              $('#process-progress').addClass('progress-bar-danger active');
              $('#process-progress').html("Processing search");
          }
        }
      }, false);
      return xhr;
    },
    success: completeHandler = function(data) {
      switch (data.result) {
        case 'success':
          setpage(data);
          console.log('Success!');
          break;
        case 'no results':
          alert("No search results!");
          resetpage();
          break;
        default:
          alert("Something went wrong!");
          resetpage();
      }
      isSubmitting = false;
    },
    error: errorHandler = function() {
      isSubmitting = false;
      resetpage();
      alert("Something went wrong!");
    },
    data: JSON.stringify(data),
    dataType: 'json',
    cache: false,
    contentType: false,
    processData: false
  }, 'json');
};
