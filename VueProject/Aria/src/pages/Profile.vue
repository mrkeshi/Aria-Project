<template>
          <section class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-8 lg:w-3/5">
                    <div class="w-full">
                   
        
                        <form class=" flex flex-col" @submit.prevent="update">
                            <h2 class="font-bold text-base text-gray-600"> اطلاعات فردی</h2>
                            <div class="grid grid-cols-1 gap-6 mt-4 md:grid-cols-2">

                          
                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">نام</label>
                                <input required v-model="user.firstname" type="text" placeholder="علیرضا" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                            </div>
        
                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">نام خانوادگی</label>
                                <input required v-model="user.lastname" type="text" placeholder="کشاورز" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                            </div>
        
                            <div>
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">شماره تلفن</label>
                                <input minlength="11" v-model="user.phone" type="text" placeholder="09907881747" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                            </div>
                            <div class="w-full ">
                                <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">آدرس ایمیل</label>
                                <input v-model="user.email" type="email" placeholder="paressep28@gmail.com" disabled class="block opacity-50 w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                            </div>
                          
                        </div>
                        <div class="w-full mt-6">

                        <label class="block mb-4 text-sm font-medium text-gray-900 dark:text-white" for="file_input">آپلود آواتار</label>
                        <input type="file" @change="handleFileUpload"
                       style="margin-bottom: 10px;" class="w-full  text-gray-500 font-medium text-sm file:py-4 bg-gray-100 file:cursor-pointer cursor-pointer file:border-0  file:px-4  file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" placeholder="s" />
                
                        <a v-if="user.avatar" :href="user.avatar" style="color: #3b82f6;" class="mt-1 text-blue-500 mt-2 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">آواتار فعلی:

                   
                </a>
                <span v-if="user.avatar" @click="delprof" class="text-sm"  style="color: red;cursor: pointer;">
                         (حذف آواتار)
                    </span>
</div>
                         

<br>
                                        <div class="">
                                            <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">درباره من</label>
                                           
                                                <textarea v-model="user.about" class="block w-full px-5 py-3 mt-2 text-gray-700 text-sm placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" rows="5" placeholder="این اطلاعات در مورد شما می باشد"></textarea>
                                      
                                        </div>

                              
                                <div class="float-left sve-bt mt-4" >
                                    <button  :class="[
                                  'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                  loading ? ' disabled' : ''
                              ]" :disabled="loading">
                                        <span>ذخیره اطلاعات</span>
                
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                                        </svg>
                                    </button>
                                </div>
                          
                            <div class="mt-6 text-center ">
                                <RouterLink :to="{name:'forgot'}" class="text-sm text-blue-500 hover:underline dark:text-blue-400">
                               می خواهم رمز عبور را تغییر دهم
                                </RouterLink>
                            </div>
                        </form>
                    
                    </div>
                </div>
            </section>

  </template>
  
  <script setup>
  import { onMounted, reactive, ref } from 'vue'
  import { RouterLink } from 'vue-router';
  import { useToast } from "vue-toastification";
  import { getDetailuser } from '@/services/user';
import { useAuthStore } from '@/stores/auth';
import { useUserStore } from '@/stores/user';
const auth=useAuthStore()
const userstore=useUserStore()
  const loading = ref(false)
  const toast = useToast();
  const selectedFile=ref(null);
  const user = reactive({
      firstname: '',
      lastname: '',
      phone:'',
      about:'',
        email:'',
  });
 
  const loginEvent = async () => {
      if (!loading.value) {
          loading.value=true
          await User.loginActions(user.email,user.password)
          loading.value=false
     
      }
  
  }

  let av=null
  function handleFileUpload(event) {
    av = event.target.files[0];
  
    }

  onMounted (async ()=>{
  
    await getDetailuser(auth.user.access).then((data)=>{
     user.firstname=data.data.first_name
       user.lastname=data.data.last_name
        user.phone=data.data.phone
        user.email=data.data.email
        user.about=data.data.about
        user.avatar=data.data.avatar

    }).catch((da)=>{
        console.log(da)
       })
  })

  
  const update=async ()=>{
    if (!loading.value) {
    loading.value=true
    await userstore.updateProfileAction(user,av)
loading.value=false
  }
}
function delprof(){
    av=''
}
  </script>
  
  <style>
  .sve-bt{
    display: flex;
    flex-direction: row-reverse;
    float: right !important;
  }
  .sve-bt button{
    font-size: 14px;
  }
  </style>