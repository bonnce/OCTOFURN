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
              $("#client-table tbody").html(data.html_lista_cliente);
              $("#modal-client").modal("hide");
            }
            else {
              $("#modal-client .modal-content").html(data.html_form);
            }
          }
        });
        return false;
      };
    var loadForm=function () {
      var btn=$(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-client").modal("show");
        },
        success: function (data) {
          $("#modal-client .modal-content").html(data.html_form);
        }
      });
    };
    var search= function(){
        v=$(this).val()
        if(v==""){
          v="~"
        }
        $.ajax({
          url: "/Clientes/"+v+"/buscarC",
          data: "client",
          type: "get",
          dataType: 'json',
          success: function (data) {
              $("#client-table tbody").html(data.html_lista_cliente);
          }
        });
      };
    //crear
    $(".js-create-client").click(loadForm);
    $("#modal-client").on("submit",".js-client-create-form",saveForm);
    //editar
    $("#client-table").on("click",".js-update-client",loadForm);
    $("#modal-client").on("submit",".js-client-update-form",saveForm);
    //borrar
    $("#client-table").on("click",".js-delete-client",loadForm);
    $("#modal-client").on("submit",".js-client-delete-form",saveForm);
    //buscar
    $(".js-search-client").on("input",search);
  });