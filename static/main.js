$(document).ready(function () {
  $(function getData() {
    $.getJSON("/ajax/fetch", function (data) {
      $("#artist-text").text(data.song_artists);
      $("#title-text").text(data.song_name);
      $("#cover").attr("src", data.song_cover);
    });
  });
});
