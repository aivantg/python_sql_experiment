function new_post(){
  $.ajax({
    type: "POST",
    url: "/create",
    data: { title: "Hello world", description: "Desciption"}
  }).done(function( o ) {
     console.log(o)
  });
}
