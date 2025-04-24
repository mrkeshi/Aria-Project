<template>

    <div>
    
        
        <section>
            <div class="row flex mt-8 max-lg:mt-6 justify-between w-full px-2 py-6 items-center max-lg:felx-col  max-lg:flex-wrap ">
                    <div class="flex items-center max-lg:hidden ">
                                <img class="h-28 max-lg:h-20" src="/assets/media/ask_answer.png" alt="">
                                <h2 class="text-3xl font-bold text-gray-600 max-lg:text-xl">ویرایش پرسش  </h2>
                            </div>

                       
            </div>
        </section>
            
        <section>
            <div class="row my-4 max-lg:mt-4  w-[90%] flex flex-col  mx-auto justify-center max-lg:w-full max-lg:px-4">
                <div class="questions w-full shadow-sm bg-white rounded-2xl mt-6 ">
                        <div class="header w-full justify-between p-8 max-lg:p-4 flex items-center ">
                                <div class="flex flex-row items-center">
                                            <img v-if="user.user.avatar" :src="user.user.avatar" style="width: 72px;" class="h-[72px]  max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-green-500" alt="">
                                            <img v-else src="/assets/media/prof.png" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-green-500" alt="">

                                            <div>
                                                <h3 v-if="user.user.firstname" class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{user.user.firstname+' '+user.user.lastname}}</h3>
                                                <h3 v-else class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{'بدون نام'+ "|"+user.user.email}}</h3>

                                                <span href="#" class="text-blue-400 text-sm"> 
                                                  <b>تخصص: </b>
                                                  <span v-if="user.user.current_project">
                                                    <span v-if="user.user.level==1">مدیر پروژه</span>
    <span v-else-if="user.user.level==2" style="width: auto;"> کارمند ارشد {{ user.user.rollname }} </span>
        
    <span v-else="user.user.level==2"> کارمند {{ user.user.rollname }}  </span>
                                                  </span>
                                                {{  }}
                                                </span>
                                            </div>
                                        </div>
                               
                            
                        </div>
                        <div class="max-lg:p-5">
                        <div class="max-lg:w-full  w-5/6 mx-auto bg-blue-100 p-4 rounded-md border border-blue-500 flex justify-center flex-col">
                            <b class="text-blue-600">قبل از ویرایش پرسش دقت کنید</b>
                            <p class="text-blue-500 mt-3">
                              ۱- از ارسال پرسش تکراری خودداری کنید.
                            </p>
                            <p class="text-blue-500 mt-2">
۲- شما مجاز به آپلود فقط یک فایل هستید پس لطفا  در صورتی که بیش از چندفایل دارید لطفا آن ها را zip کرده و بارگذاری نمایید.
                            </p>
                        </div>
                      

                        </div>
                        <form @submit.prevent="send"   class="mt-4 max-lg:mt-1 p-8 w-full max-lg:p-6">

                 
                            <div class="flex max-lg:flex-col w-full">
                              <div class="w-1/2 lg:mx-2 max-lg:w-full">
                                <label  for="countries" class="block font-bold text-gray-700 text-2xl max-lg:text-xl dark:text-white mb-4">عنوان پرسش</label>
                                <input v-model="IssuesStore.singleIssues.subject" class="w-full h-16 rounded-md p-6 bg-[#f3f3f3] focus:outline-blue-500  border border-gray-300 text-gray-600  border " type="text" placeholder="این عنوان پرسش شما می باشد">
                              </div>
                              <div class="w-1/2 lg:mx-2 max-lg:w-full max-lg:mt-6">
                                
                            <label for="countries" class="block font-bold text-2xl max-lg:text-xl  text-gray-700 dark:text-white mb-4">تسک خود را انتخاب کنید</label>
                            <select v-model="IssuesStore.singleIssues.task"  id="countries" class="h-16  text-[16px] text-gray-600 bg-[#f3f3f3]  selection:ring-blue-500 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                              <option   v-for="task in taskStore.tasks" :value="task.id">{{ task.title }}</option>
                              <option  value=null >تعریف نشده</option>
                           
                            </select>
                              </div>
                            </div>
                            <div class="flex justify-center p-2">
                              <textarea v-model="IssuesStore.singleIssues.description" rows="5" id="" class="w-full  mt-4 bg-[#f3f3f3] border  rounded-lg border-gray-300 focus:border-blue-500 p-4 text-gray-600 outline-blue-500" placeholder="چیزی برای نوشتن وارد کنید"></textarea>

                            </div>
                            <div class="w-full mt-3 mb-6 px-2">
                             
                             <label class="block font-bold text-2xl max-lg:text-xl  text-gray-700 dark:text-white mb-4"> آپلود مستندات ( اختیاری)</label>
                           
                             <input @change="handleFileUpload" class="block w-full mb-5 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer p-3 bg-[#f3f3f3] dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="default_size" type="file">                            </div>
                             <div v-if="IssuesStore.singleIssues.assigned_attached" >
                                <div style="align-items: end;" class="flex">

                               
                                <a :href="IssuesStore.singleIssues.assigned_attached" style="padding-left: 6px;" class="text-blue-500 px-8 flex items-center mt-4">
                          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.125 2.25h-4.5c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125v-9M10.125 2.25h.375a9 9 0 019 9v.375M10.125 2.25A3.375 3.375 0 0113.5 5.625v1.5c0 .621.504 1.125 1.125 1.125h1.5a3.375 3.375 0 013.375 3.375M9 15l2.25 2.25L15 12"></path>
                        </svg> 
                          <span class="mx-1">
                              فایل سنجاق شده فعلی</span>
                            
                            </a>
                              <span @click="delfile" style="cursor: pointer;" class="text-red-500">(حذف)</span>
                             </div>
                            </div>
                              <div class="w-full flex justify-end">
                              <button  :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                loading ? ' disabled' : ''
                            ]" :disabled="loading">ثبت پرسش</button>
                            </div>
                        </form>

                     <br><br>
                    
                </div>
            </div>
        </section>
    </div>
    
    </template>
    

    
    <script setup>

import router from '@/router';
import { useAuthStore } from '@/stores/auth';
import { useIssuesStore } from '@/stores/IssuesStore';
import { useTaskStore } from '@/stores/TaskStore';
import { useUserStore } from '@/stores/user';
import { onMounted, reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';


const loading = ref(false)
const route=useRoute()
const IssuesStore=useIssuesStore()
let av=null
  function handleFileUpload(event) {
    av = event.target.files[0];
  
    }
    const user=useUserStore()
    const taskStore=useTaskStore()
    onMounted(async()=>{
      await taskStore.ShowallTaskAction()
     await IssuesStore.getSingleIssues(route.params.id,user.user.current_project)
     if(IssuesStore.singleIssues.creator!=user.user.id){
        const toast=useToast()
        toast.error('شما به این صفحه دسترسی ندارید')
        router.push("/discuss/")
     }
    })
    const issues=reactive({
      id:'',
      title:'',
      description:'',
      task:null
    })
   async function send(){
    if (!loading.value) {
        issues.id=IssuesStore.singleIssues.id
        issues.title=IssuesStore.singleIssues.subject
        issues.description=IssuesStore.singleIssues.description
        issues.task=IssuesStore.singleIssues.task

        loading.value=true
        console.log(issues.task)
        if(issues.task==null || issues.task=='null'){
          issues.task=''
        }
        user.user.current_project
       
        await IssuesStore.editIssues(issues,av,issues.id,user.user.current_project)
        loading.value=false
   
    }
  }
  function delfile(){
    IssuesStore.singleIssues.assigned_attached=''
    av=''
  }

    </script>
    
    <style>
    
    </style>