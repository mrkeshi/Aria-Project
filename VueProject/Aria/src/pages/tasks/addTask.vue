<template>
    <div>
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
                <h1 class="text-gray-700 font-bold text-xl">اضافه کردن تسک جدید</h1>
                <p class="text-gray-600 text-sm text-wrap">شما در این قسمت می توانید تسک جدیدی به پروژه اضافه کنید</p>
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                        <button  v-if="userstore.user.level==1" class="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-orange-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z"></path>
                              </svg>
                              
                            <RouterLink :to="{name:'user'}" class="mx-1 text-sm">مدیریت کاربران</RouterLink>
                        </button>
                        <button class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-green-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122"></path>
                              </svg>                          
                            
                            <RouterLink style="color: white;" :to="{name:'task'}" class="mx-1 text-sm">مدیریت وظایف</RouterLink>
                        </button>
                    </div>
                </div>    
            </div>
           
          
            <section v-if="skills[0]" class=" w-full px-4 mx-auto ">
                <div class="flex items-center shadow-md mt-8 max-lg:mt-4 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="w-full">

        
                        <form @submit.prevent="send" class="flex flex-col ">
                            <h1 class="text-gray-700 mb-2 text-base dark:text-gray-300 font-bold">مشخص کردن کاربر </h1>
                            <div class="mt-4">
                                <div class="w-full ">   
                                    
                       
                                    <label class="block mb-1 text-sm text-slate-800">
                                       حوزه کاری 
                                    </label>
                                   
                                    <div class="relative w-full">
                                   
                                      <select @change="getUsersWithSkil"  v-model="createskil"  required class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border px-5 py-3 border-slate-200 rounded pl-3 pr-8 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md appearance-none cursor-pointer">
                                          <option v-for="skil in skills" :value="skil.id" :selected="createskil==skil.id">{{ skil.name }}</option>
                                     
                                    
                                      </select>
                                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="currentColor" class="h-5 w-5 ml-1 absolute top-2.5 right-2.5 text-slate-700">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9"></path>
                                      </svg>
                                    </div>
                                    <p class="flex items-center mt-2 text-xs text-slate-500">
                                 
                                    </p>
                                  </div>
                            </div>
                            <div v-if="users[0]" class="mt-4"> <label class="block mb-1 text-sm text-slate-800">
                                      کاربر
                                    </label>
                                <div class="relative w-full">
                                   
                                    <select  required :value="task.assigned" v-model="task.assigned" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border px-5 py-3 border-slate-200 rounded pl-3 pr-8 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md appearance-none cursor-pointer">
                                        <option v-for="user in users" :selected="task.assigned==user.id" :value="user.id">
  {{ user.email }} |
  {{
    user.first_name && user.last_name
      ? user.first_name + ' ' + user.last_name
      : user.first_name
      ? user.first_name
      : user.last_name
      ? user.last_name
      : 'ناشناس'
  }}
</option>                                  
                                    </select>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="currentColor" class="h-5 w-5 ml-1 absolute top-2.5 right-2.5 text-slate-700">
                                      <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9"></path>
                                    </svg>
                                  </div>                        
                            </div>
                      <h1 class="mt-4 text-red-500" style="color: red;" v-else>
هیچ کاربری وجود ندارد.
                      </h1>
                            <h1 class=" text-gray-700 mt-6  text-base dark:text-gray-300 font-bold">اطلاعات تسک </h1>
                            <div class="mt-4">
                                <label class="block  mb-1 text-sm text-slate-800">
                                     اهمیت تسک 
                                 </label>
                                
                                 <div class="relative w-full">
                                   <select  v-model="task.importance" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border px-5 py-3 border-slate-200 rounded pl-3 pr-8 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md appearance-none cursor-pointer">
                                       <option value="1" >مهم</option>
                                       <option  value="2">متوسط</option>
                                       <option value="3">کم اهمیت</option>

                                   </select>
                                   <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="currentColor" class="h-5 w-5 ml-1 absolute top-2.5 right-2.5 text-slate-700">
                                     <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9"></path>
                                   </svg>
                                 </div>
                                </div>
                                <div class="mt-4">
                                    <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">عنوان تسک</label>
                                    <input required type="text" v-model="task.title" placeholder=" تسک آزمایشی" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                                </div>
                                <div class="mt-4">
                                    <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">زمان تحویل</label>
                              
                                    <input data-jdp-min-date="today" required data-jdp="" data-jdp-miladi-input="miladi_date" placeholder="1382/02/12" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40">
                                    <input id="miladi_date" hidden >
                                </div>
                                <div class="mt-4">
                                    <label class="block mb-2 text-base text-gray-700 dark:text-gray-200">توضیحات </label>
                                    <textarea v-model="task.description" rows="5" placeholder="توضیحات اختیاری" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"></textarea>
                                </div>
                         
                                <div class="w-full mt-6">

                                    <h1 class="block mb-4  font-extrabold text-gray-900 dark:text-white" for="file_input">آپلود مستندات (اختیاری)</h1>
                                    <input type="file" @change="handleFileUpload" class="w-full  text-gray-500 font-medium text-sm file:py-4 bg-gray-100 file:cursor-pointer cursor-pointer file:border-0  file:px-4  file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" placeholder="s">
                            <p class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">لطفا در صورت نیاز مستندات لازم را آپلود نمایید.</p>
            </div>
                              
                            <div class="w-full float-left">
                                <button v-show="!loading"  style="font-size: 14px !important;margin-top: 20px;float: left;" 
                                :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">
                                <span> ساخت تسک </span>
        
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                                </svg>
                            </button>
                            </div>
                          
                        </form>
                    </div>
                </div>
            </section>
            <h2 v-else>شما هیچ کاربری را به پروژه اضافه نکرده اید.</h2>
    </div>
    </template>
    <script setup>

import { onMounted, reactive, ref, watch } from 'vue'
import { useAuthStore } from '@/stores/auth';
const createskil=ref()
const users=reactive({})
const  skills=reactive({})

const auth=useAuthStore()
const userstore=useUserStore()
import { RouterLink, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';
import { useTaskStore } from '@/stores/TaskStore';
import { getSkils } from '@/services/skil';
import { getUserWithSkilService } from '@/services/TaskServices';
import { useToast } from 'vue-toastification';
const taskStore=useTaskStore();
const loading = ref(false)




async function  getUsersWithSkil()  {
  
   await getUserWithSkilService(auth.user.access,createskil.value).then((response)=>{
  
    Object.keys(users).forEach(key => delete users[key]);
    Object.assign(users,{...response.data})
       if(skills[0]){
   
       
       if(users[0]){
    
        task.assigned=users[0].id
       }
    }
    }).catch((er)=>console.log(er))
}

onMounted(async()=>{
    if(userstore.user.level>2){
        toast.warning("شما به این صفحه دسترسی ندارید")
        router.push('/dashboard/')
    }
    await getSkils(auth.user.access).then((data)=>{
        Object.assign(skills,{...data.data})
    })

    if(skills[0]){
       createskil.value=skills[0].id 
       
      await getUsersWithSkil()
   

       if(users[0]){
     
        task.assigned=users[0].id
       }
    }
  
    document.querySelector("[data-jdp-miladi-input]").addEventListener("jdp:change", function (e) {
    var miladiInput = document.getElementById(this.getAttribute("data-jdp-miladi-input"));
    if (!this.value) {
        miladiInput.value = "";
        return;
    }
    
    var dateTime = this.value.split(" ");
    var date = dateTime[0].split("/");
    var time = dateTime[1] ? dateTime[1].split(":") : ["00", "00", "00"];
    

    var gregorianDate = jalali_to_gregorian(date[0], date[1], date[2]);

    miladiInput.value = gregorianDate.join("/") + " " + time[0] + ":" + time[1] + ":" + time[2];
});

function jalali_to_gregorian(jy, jm, jd) {
    jy = Number(jy);
    jm = Number(jm);
    jd = Number(jd);
    var gy = (jy <= 979) ? 621 : 1600;
    jy -= (jy <= 979) ? 0 : 979;
    var days = (365 * jy) + ((parseInt(jy / 33)) * 8) + (parseInt(((jy % 33) + 3) / 4))
        + 78 + jd + ((jm < 7) ? (jm - 1) * 31 : ((jm - 7) * 30) + 186);
    gy += 400 * (parseInt(days / 146097));
    days %= 146097;
    if (days > 36524) {
        gy += 100 * (parseInt(--days / 36524));
        days %= 36524;
        if (days >= 365) days++;
    }
    gy += 4 * (parseInt((days) / 1461));
    days %= 1461;
    gy += parseInt((days - 1) / 365);
    if (days > 365) days = (days - 1) % 365;
    var gd = days + 1;
    var sal_a = [0, 31, ((gy % 4 == 0 && gy % 100 != 0) || (gy % 400 == 0)) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var gm;
    for (gm = 0; gm < 13; gm++) {
        var v = sal_a[gm];
        if (gd <= v) break;
        gd -= v;
    }
    return [gy, gm, gd];
}
   
  })

jalaliDatepicker.startWatch({
    'time': true ,
      minDate: "attr",
  maxDate: "attr"
});




const task = reactive({
      title: '',
      project: '',
      description:'',
      finished_at:'',
      importance:1,
      assigned:'',

  });


const send = async () => {
    task.project=userstore.user.current_project

    if (!loading.value) {
        loading.value=true
        task.finished_at=document.getElementById('miladi_date').value
        let date = new Date(task.finished_at.replace(/-/g, '/'));  
        task.finished_at = date.toISOString();
        await taskStore.addtaskAction(task,av)
        loading.value=false
   
    }
   


}


let av=null
  function handleFileUpload(event) {
    av = event.target.files[0];
  
    }


  
    </script>

    <style >

.active{
    background-color: #3b82f6;
    color: white;
}
    </style>