$(function () {

  const $form = $("#search-form");
  const $input = $("#search-value");
  const $results = $("#search-results");

  $form.submit(function (e) {
    e.preventDefault();
    $.getJSON(
      "/search",
      { q: $input.val() },
      function (documents) {
        $results.empty();
        documents.forEach(function (document) {
          $results.append(`
            <li id=${document.id}>
              [ <a href="/similar?id=${document.id}">${document.id}</a> ]
              ${document.take_txt_en}
            </li>`);
        })
      }
    );
  });
});
