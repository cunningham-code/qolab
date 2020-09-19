/*

Home Components

*/
Vue.component("home-header", {
  props: ["title", "icon"],
  template:
    '<div class="row header"><div class= "icon-container"><i class="fas fa-chart-bar"></i></div><h2 style="margin: 0;" class="title-text">{{ title }}</h2></div >',
});

x = new Vue({
  delimiters: ["[[", "]]"],
  el: "#app",
  data: {
    test: "I love Max!!!",
    message: "You loaded this page on " + new Date().toLocaleString(),
  },
});
