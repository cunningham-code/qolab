x = new Vue({
  delimiters: ["[[", "]]"],
  el: "#app",
  data: {
    test: "I love Max!!!",
    message: "You loaded this page on " + new Date().toLocaleString(),
  },
});
