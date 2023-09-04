import { createApp } from 'vue';
import ApplicationCard from "./components/ApplicationCard";
// Vuetify
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'
import RegistrationDisabledDialog from "./components/RegistrationDisabledDialog";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
})

const app = createApp({});
app.config.compilerOptions.delimiters = ['[[', ']]'];
app.component("application-card", ApplicationCard);
app.component("registration-disabled-dialog", RegistrationDisabledDialog)
app.use(vuetify).mount('#app');
