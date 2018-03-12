$(window).on('load', function() {
//Linear easing
function linear (duration, range, current) {
  return ((duration * 2) / Math.pow(range, 2)) * current;
}
function animateValue(id, start, duration, easing) {
  var end = Number(id.text())
  var range = end - start;
  var current = start;
  var increment = end > start? 1 : -1;
  var startTime = new Date();
  var offset = 1;
  var remainderTime = 0;
  var step = function() {
    if (current < end) {
    current += increment;
    id.text(current+"%");
    }
    if (current != end) {
      setTimeout(step, easing(duration, range, current));
    }
  };
  
  setTimeout(step, easing(duration, range, start));
}

$('.perc').each(function(){
animateValue($(this), 0, 1000, linear);

});
 $(".btn").click(function(){ 
    survey= $(this).attr("survey");
    option= $(this).attr("option");
    votos= $(this).attr("votos");
$.ajax({
  url:'/api/vote/survey='+survey+'/option='+option,
  type:'POST',
    data: {
            csrfmiddlewaretoken: csrf_token
        },
});
 setInterval(function() {
                  location.reload();
                }, 60000);  });


  }); 



