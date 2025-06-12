
import './assets/main.css'
import './assets/style.css'
import './assets/customstyle.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import 'sweetalert2/dist/sweetalert2.min.css';
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(Toast,{
    rtl: true,
  
})
app.mount('#app')
