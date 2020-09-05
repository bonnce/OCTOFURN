$(function () {    
  var saveForm= function () {
    var form = $(this);
    
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#table tbody").html(data.html_lista);
          $("#modal").modal("hide");
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };
var loadForm=function () {
  var btn=$(this);
  console.log(btn)
  $.ajax({
    url: btn.attr("data-url"),
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal").modal("show");
    },
    success: function (data) {
      $("#modal .modal-content").html(data.html_form);
    }
  });
};
var search= function(){
    var form=$(this);
    console.log(form,form.attr("action"),form.serialize(),form.attr("method"));
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {       
        $("#table tbody").html(data.html_lista);
      }
    });
  };
  //crear
  $(".js-create").click(loadForm);
  $("#modal").on("submit",".js-create-form",saveForm);
  //editar
  $("#table").on("click",".js-update",loadForm);
  $("#modal").on("submit",".js-update-form",saveForm);
  //borrar
  $("#table").on("click",".js-delete",loadForm);
  $("#modal").on("submit",".js-delete-form",saveForm);
  //buscar
  $(".js-search-form").on("input",search);
});