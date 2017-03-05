(function(){
  $(document).ready(function(){
  $("#submit-button").click(function(){
    $.ajax({
      url: "/scores",
      type: "POST",
      data: JSON.stringify({
        name: $('#name').val(),
        score: GAME_SCORE
      }),
      dataType: "json",
      contentType: "application/json"
    })
    .done(function (data) {
      var boardContent = data.scores.map(function(score){
        return "<li><div class='name'>" + score[0] + "</div><div class='score'>" + score[1] + "</div></li>";
      }).join('');

      $('.leaderboard .scores').html(boardContent);

    });
  });
});
