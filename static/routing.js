function new_post(){
  $.ajax({
    type: "POST",
    url: "http://localhost:5000/create",
    data: { title: "Hello world", description: "Desciption"}
  }).done(function( o ) {
     console.log(o)
  });
}
