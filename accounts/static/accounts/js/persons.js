$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-person").modal("show");
      },
      success: function (data) {
        $("#modal-person .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#person-table tbody").html(data.html_person_list);
          $("#modal-person").modal("hide");
        }
        else {
          $("#modal-person .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create person
  $(".js-create-person").click(loadForm);
  $("#modal-person").on("submit", ".js-person-create-form", saveForm);

  // Update person
  $("#person-table").on("click", ".js-update-person", loadForm);
  $("#modal-person").on("submit", ".js-person-update-form", saveForm);

$("#person-table").on("click", ".js-delete-person", loadForm);
$("#modal-person").on("submit", ".js-person-delete-form", saveForm);

});