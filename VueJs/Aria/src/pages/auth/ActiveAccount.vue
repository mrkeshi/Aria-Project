<template>
    <div class="row flex">
          
     
          <div class="main px-6 py-8 flex flex-col w-[calc(95%-320px)] max-lg:w-full mx-auto -z-0 relative">
              <section class=" ">
                  <div class="container flex lg:mt-12 mt-6 min-h-screen px-6 py-6 mx-auto">
                      <div class="flex flex-col items-center max-w-sm mx-auto text-center">
                          <p class="p-3 text-sm font-medium text-blue-500 rounded-full bg-blue-50 dark:bg-gray-800">
                              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5m8.25 3v6.75m0 0-3-3m3 3 3-3M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"></path>
                                </svg>
                                
                          </p>
                          <h1 class="mt-3 text-2xl font-semibold text-gray-800 dark:text-white md:text-3xl">اکانت شما فعال نیست</h1>
                          <p class="mt-4 text-gray-500 dark:text-gray-400">متاسفانه اکانت شما فعال نشده استو لطفا صندوق ایمیل را چک کنید.</p>
              
                          <div class="flex items-center w-full mt-6 gap-x-3 shrink-0 sm:w-auto">
                              <button @click="logout" class="flex items-center justify-center w-1/2 px-5 py-2 text-sm text-gray-700 transition-colors duration-200 bg-white border rounded-lg gap-x-2 sm:w-auto dark:hover:bg-gray-800 dark:bg-gray-900 hover:bg-gray-100 dark:text-gray-200 dark:border-gray-700">
                                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 rtl:rotate-180">
                                      <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18"></path>
                                  </svg>
              
              
                                  <span>خروج</span>
                              </button>
              
                              <button @click="fresh" class="w-1/2 px-5 py-2 text-sm tracking-wide text-white transition-colors duration-200 bg-blue-500 rounded-lg shrink-0 sm:w-auto hover:bg-blue-600 dark:hover:bg-blue-500 dark:bg-blue-600">
                                  ارسال لینک فعالسازی
                              </button>
                          </div>
                      </div>
                  </div>
              </section>
    
    
          </div>
    
          
    
      </div>
    </template>
    
    <script setup>
    import { reactive, ref } from 'vue'
    import { RouterLink } from 'vue-router';
    import { useAuthStore } from '@/stores/auth';
    import { useUserStore } from '@/stores/user';
    import { useToast } from "vue-toastification";
    import router from '@/router';
    const Auth=useAuthStore()
    const User=useUserStore()
    const toast = useToast();
    console.log(User.user)
    if(User.user.isactive || !Auth.user.email){
        toast.warning("شما مجوز ورود به این صفحه را ندارید")
        router.push('/login')
    }

    
    const fresh = async () => {
        if (!loading.value) {
            loading.value=true
            await User.active(Auth.email)
            loading.value=false
    
        }
    
    }


function logout(){
    Auth.logoutAction()
}
    </script>
    
    <style>
    </style>