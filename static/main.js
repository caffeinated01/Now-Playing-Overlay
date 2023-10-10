const INTERVAL = 5; // In seconds

$(document).ready(function () {
  $(function getCover() {
    $.getJSON("/ajax/covers", function (data) {
      $("#cover").attr("src", data.cover);
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
  }, INTERVAL * 1000); // Interval between check
});
