var API_TOKEN = document.getElementById('API_TOKEN').value;
var butter = Butter(API_TOKEN);
var app = new Vue({
  el: '#app',
  data: {
    body: '',
    name: '',
    heroImage: ''
  },
  mounted: function(){
    butter.page.retrieve('*', 'sample-page').then((resp)=>{
        const data = resp.data.data;
        const fields = data.fields;
        this.body = fields.body;
        this.name = data.name;
        this.heroImage = fields.hero_image;
    });
  }
});

