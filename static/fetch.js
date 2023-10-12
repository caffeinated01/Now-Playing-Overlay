$(document).ready(function () {
  $(function getBase() {
    $.getJSON("/ajax/onload", function (data) {
      $("#cover").attr("src", data.cover);
      $("#artist-text").css("color", data.artist_color);
      $("#title-text").css("color", data.title_color);
      $("#box").css("background-color", data.background_color);
      $("#box").css("min-width", data.width);
    });
  });
  function getData() {
    $.getJSON("/ajax/fetch", function (data) {
      $("#artist-text").text(data.song_artists);
      $("#title-text").text(data.song_name);
      $("#cover").attr("src", data.song_cover);
    });
  }
  setInterval(function () {
    getData();
  }, 5 * 1000); // Interval between check
});
