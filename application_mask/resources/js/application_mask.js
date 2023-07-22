import { createApp } from 'vue';
import ApplicationCard from "./components/ApplicationCard";

// Vuetify
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

const app = createApp({});
app.config.compilerOptions.delimiters = ['[[', ']]'];
app.component("application-card", ApplicationCard);
app.use(vuetify).mount('#app');
