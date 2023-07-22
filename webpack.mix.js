let mix = require('laravel-mix');
require('vuetifyjs-mix-extension')
let staticPath = "application_mask/static/build";
let resourcesPath = "application_mask/resources";

mix.setResourceRoot("/static/build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath("application_mask/static"); // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes("--browser-sync")) {
  mix.browserSync("localhost:8000");
}
mix.copy('node_modules/@mdi/font/fonts/', 'dist/fonts/')
// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.js(`${resourcesPath}/js/application_mask.js`, `${staticPath}/`).vuetify().vue();
mix.sass(`${resourcesPath}/sass/application_mask.scss`, `${staticPath}/`);