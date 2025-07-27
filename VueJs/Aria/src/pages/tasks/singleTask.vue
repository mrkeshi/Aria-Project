<template>
    <div>
        <div class=" px-x py-8 flex flex-col w-[calc(95%-320px)] max-lg:w-full mx-auto -z-0 relative">
            
            <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8 px-4 ">
             
             
                <div class="flex w-full flex-wrap max-md:justify-center justify-end mx-2 mt-6 ">
              
                    <div class="flex flex-wrap ">
                    
                        <button class="flex items-center mx-2 px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-green-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 0 1 2.25-2.25h7.5A2.25 2.25 0 0 1 18 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 0 0 4.5 9v.878m13.5-3A2.25 2.25 0 0 1 19.5 9v.878m0 0a2.246 2.246 0 0 0-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0 1 21 12v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6c0-.98.626-1.813 1.5-2.122"></path>
                              </svg>                          
                            
                            <RouterLink :to="{name:'task'}" style="color: white;"  class="mx-1 text-sm">مدیریت وظایف</RouterLink>
                        </button>
                    </div>
                </div>    
            </div>
           

       </div>
            <section   class=" w-full px-4 mx-auto ">
                <div class="flex flex-col shadow-md mt-8 max-lg:mt-4 border-t-4 border-green-500 bg-white w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                    <div class="col p-4 mt-2 flex">
                        <h2 class="text-gray-800 font-bold"> عنوان تسک :</h2>
                        <span class="text-blue-500 px-2">{{ taskStore.task.title }}</span>
                    </div>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold">  تعریف کننده:</h2>
                        <span class="text-blue-500 px-2">{{creator.email }} | <span v-if="creator.last_name">{{ creator.first_name+ ' '+ creator.last_name }}</span> </span>
                    </div>
                    <!-- <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold">  کاربر انجام دهنده  :</h2>
                        <span class="text-blue-500 px-2">{{ task.assigned.email }} | <span v-if="task.assigned.first_name">{{ task.assigned.first_name  }}</span>  <span v-if="task.assigned.last_name">{{ task.assigned.last_name }}</span> </span>     
                                   </div> -->
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> توضیحات  :</h2>
                        <span class="text-blue-500 px-2">{{ taskStore.task.description }}</span>
                    </div>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> درجه اهمیت   :</h2>
                        <span v-if="task.importance==1" class=" px-2 mx-2 bg-red-500 text-white rounded-sm px-2 "> مهم</span>
                        <span v-else-if="task.importance==2" class=" px-2 mx-2 bg-orange-500 text-white rounded-sm px-2 "> متوسط</span>
                        <span v-else class=" px-2 mx-2 bg-green-500 text-white rounded-sm px-2 "> کم اهمیت</span>

                    </div>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold">  وضعیت تسک   :</h2>
                        <span v-if="!task.done" class=" px-2 mx-2 bg-red-500 text-white rounded-sm px-2 "> باز</span>
                        <span v-else class=" px-2 mx-2 bg-green-500 text-white rounded-sm px-2 "> بسته </span>

                    </div>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> تاریخ ایجاد  :</h2>
                        <span class="text-blue-500 px-2" v-text="convertToJalali(taskStore.task.created_at)"> </span>
                    </div>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> تاریخ خاتمه  :</h2>
                        <span class="text-blue-500 px-2 " v-text="convertToJalali(taskStore.task.finished_at)"> </span>
                    </div>
                    <hr>
                    <div class="col p-4 mt-2 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> امتیاز   :</h2>
                        <span class="text-blue-500 px-2 " v-if="taskStore.task.rate">{{taskStore.task.rate}}</span>
                        <span class="text-blue-500 px-2 " v-else>بدون امتیاز</span>

                    </div>
                    <div class="col p-4 mb-4 flex flex-row">
                        <h2 class="text-gray-800 font-bold"> بازخورد   :</h2>
                        <p class="text-blue-500 px-2 " v-if="taskStore.task.owner_note">{{ taskStore.task.owner_note }}  
                    </p>
                    <p class="text-blue-500 px-2 " v-else>فعلا بدون بازخورد 
                    </p>
                </div>
                    <hr>
                    <div  v-if="taskStore.task.attached" class="mt-4 flex flex-row items-center">
                     
                        <h2 class="text-gray-800 font-bold "> مستندات کاربر تعریف کننده   :</h2>
                        <a :href="'http://127.0.0.1:8000' +taskStore.task.attached" target="_blank" class="bg-blue-500 rounded-md p-2 mx-4 px-2  text-white w-40 text-center mx-auto">دانلود
                  
                        </a></div>
                    <div v-if="taskStore.task.assigned_attached" class="mt-4 flex flex-row items-center">
                     
                        <h2 class="text-gray-800 font-bold "> مستندات کاربر انجام دهنده  :</h2>
                        <a :href="'http://127.0.0.1:8000' + taskStore.task.assigned_attached" target="_blank" class="bg-blue-500 rounded-md p-2 mx-4 px-2  text-white w-40 text-center mx-auto">دانلود
                  
                        </a></div>
                </div>
            </section>


    </div>
    </template>
    
    <script setup>
const task=reactive({})
import { useAuthStore } from '@/stores/auth';
import { useUserStore } from '@/stores/user';
import { onBeforeMount, onMounted, reactive, ref } from 'vue';
import { useToast } from 'vue-toastification';
import { getDetailTask } from '@/services/TaskServices';
import { useRoute } from 'vue-router';
const toast=useToast()

const auth=useAuthStore()
const userstore=useUserStore()
const route=useRoute()
const taskStore=useTaskStore()
const load=ref(false)
const creator=reactive({})
onMounted(async ()=>{
   
     await taskStore.SingleTaskAction(route.params.id)
     Object.assign(creator,{...taskStore.task.creator})
    
})

import JDate from 'jalali-date';
import router from '@/router';
import { useTaskStore } from '@/stores/TaskStore';
function convertToJalali(isoDate) {
  const date = new Date(isoDate);

  const jDate = new JDate(date);
  const jalaliYear = jDate.getFullYear();
  const jalaliMonth = jDate.getMonth(); 
  const jalaliDay = jDate.getDate();

  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();

  return `${jalaliYear}-${jalaliMonth.toString().padStart(2, '0')}-${jalaliDay.toString().padStart(2, '0')} ` + 
         `| ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}
    </script>