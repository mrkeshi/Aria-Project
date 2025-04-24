<template>

<div v-if="loading" >
  <!-- header -->
    <section>
            <div class="row flex mt-12 max-lg:mt-8 justify-between w-full px-2 py-6 items-center max-lg:felx-col  max-lg:flex-wrap ">
                    <div class="flex items-center max-lg:hidden ">
                                <img class="h-28 max-lg:h-20" src="/assets/media/ask_answer.png" alt="">
                                <h2 class="text-3xl font-bold text-gray-600 max-lg:text-xl">مشاهده گفت و گو</h2>
                            </div>
                            <div class="flex max-lg:flex-col max-lg:w-full">

                          
                            <a  @click="closeQuestion(2)" style="cursor: pointer;display: flex;align-items: center;padding-top: 16px;padding-bottom: 16px;" v-if="IssuesStore.singleIssues.status==1 && (userStore.user.level==1 || userStore.user.id==IssuesStore.singleIssues.creator)" class="max-lg:w-full bg-yellow-500 transition hover:bg-[#f3f3f3]  py-1 border border-yellow-500 hover:text-yellow-500 max-lg:justify-center max-lg:text-center  max-lg:w-full text-white p-4 rounded-lg flex ">
                              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path>
                              </svg>
                             <span  class="mx-2">بستن گفت و گو</span> 
                            </a>
                            <a @click="closeQuestion(1)"  id="openBtn" style="cursor: pointer;display: flex;align-items: center;" v-else-if="IssuesStore.singleIssues.status==2 && (userStore.user.level==1 || userStore.user.id==IssuesStore.singleIssues.creator)" class="bg-green-500 transition hover:bg-[#f3f3f3] border border-green-500 hover:text-green-500 text-white p-4 max-lg:justify-center max-lg:text-center rounded-lg flex " >
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5V6.75a4.5 4.5 0 1 1 9 0v3.75M3.75 21.75h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H3.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
</svg>

                             <span  class="mx-2">بازکردن گفت و گو</span> 
                            </a>
                            <br>
                            <RouterLink :to="{name:'addissuess'}" class="h-16 max-lg:my-2 max-lg:w-full max-lg:justify-center max-lg:text-center ask_btn bg-blue-500 px-4 py-1 w-auto flex rounded-lg text-white items-center lg:mx-2 border-2 border-blue-500 hover:bg-[#f3f3f3] hover:text-blue-500  max-lg:text-md">
                                ثبت پرسش جدید
                                <svg class="mr-2" width="35" height="35" viewBox="0 0 42 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path class="stroke-current text-white transition duration-200 dark:group-hover:text-blue-450 group-hover:text-blue-700" d="M16.293 20.7224H21.0723M25.8517 20.7224H21.0723M21.0723 20.7224V15.943V25.5017" stroke-width="2.53025" stroke-linecap="round" stroke-linejoin="round"></path>
                                    <path class="stroke-current text-white transition duration-200 dark:group-hover:text-blue-450 group-hover:text-blue-700" opacity="0.5" d="M7.9995 20.7225C7.9995 23.6454 8.15777 25.908 8.54928 27.6696C8.93759 29.4168 9.53832 30.5928 10.3702 31.4247C11.2021 32.2566 12.3781 32.8573 14.1253 33.2456C15.887 33.6372 18.1495 33.7954 21.0725 33.7954C23.9954 33.7954 26.2579 33.6372 28.0196 33.2456C29.7668 32.8573 30.9428 32.2566 31.7747 31.4247C32.6066 30.5928 33.2073 29.4168 33.5956 27.6696C33.9871 25.908 34.1454 23.6454 34.1454 20.7225C34.1454 17.7995 33.9871 15.537 33.5956 13.7754C33.2073 12.0281 32.6066 10.8521 31.7747 10.0202C30.9428 9.18833 29.7668 8.58759 28.0196 8.19928C26.2579 7.80778 23.9954 7.64951 21.0725 7.64951C18.1495 7.64951 15.887 7.80778 14.1253 8.19928C12.3781 8.58759 11.2021 9.18833 10.3702 10.0202C9.53832 10.8521 8.93759 12.0281 8.54928 13.7754C8.15777 15.537 7.9995 17.7995 7.9995 20.7225Z" stroke-width="2.53025" stroke-linecap="round" stroke-linejoin="round">
                                    </path>
                                </svg>
                            </RouterLink>
                        </div>
            </div>
        </section>



        <!-- questions -->
        <section>
            <div class="row my-4 max-lg:mt-4  w-[90%] flex flex-col  mx-auto justify-center max-lg:w-full max-lg:px-4">
                <div style="border-top: 4px solid #6495ed;" class="questions w-full shadow-sm bg-white rounded-2xl mt-6 ">
                        <div class="header w-full justify-between p-8 max-lg:p-4 flex items-center ">
                                <div class="flex flex-row items-center">
                                            <img v-if="IssuesStore.singleIssues.creator_avatar" style="width: 72px;" :src="IssuesStore.singleIssues.creator_avatar"  class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">
                                            <img v-else src="/assets/media/prof.png"  class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">

                                            <div>
                                                <h3 class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{ IssuesStore.singleIssues.creator_name }}</h3>
                                               
                                                <a href="#" class="text-blue-400 text-sm max-lg:hidden">
                                                  <b> تخصص:</b>
                                                  <span v-if="IssuesStore.singleIssues.user_role.level ==1" >
                                                    <span v-text="IssuesStore.singleIssues.user_role.level_name"></span>
                                                  </span>    
                                                  <span v-else >
                                                    <span v-text="' '+ IssuesStore.singleIssues.user_role.level_name+' ' + IssuesStore.singleIssues.user_role.skill_name"></span>
                                                  </span>                                               
                                                </a>
                                               <span class="text-gray-600"> | </span>
                                                <a href="#" class="text-gray-400 text-sm">
                                                
                                                <RouterLink :to="{name:'singleissuess',params:{id:IssuesStore.singleIssues.id}}" class="text-yellow-400 text-sm" v-text="humanReadableTimeAgo(IssuesStore.singleIssues.updated_at) ">
                                                   
                                                </RouterLink>
                                                 </a>
                                            </div>
                                        </div>
                               
                                <div class="flex">
                                    <RouterLink :to="{name:'singleissuess',params:{id:IssuesStore.singleIssues.id}}" href="" style="width: auto;" class="flex items-center transition hover:bg-gray-500 hover:text-white rounded-lg bg-gray-200 w-[108px] max-lg:text-sm max-lg:w-28 text-gray-500 p-2.5 px-2 text-center pr-3.5 ">
                                     
                                      <span v-if="melength(IssuesStore.singleIssues.answers)>0" >{{ melength(IssuesStore.singleIssues.answers) + " پاسخ " }}</span>
                                      <span v-else >بدون پاسخ </span>
                                    </RouterLink>
                                      <a  v-if="IssuesStore.singleIssues.status==1" style="background-color: cornflowerblue;" class=" mx-2 px-6 text-white p-2 rounded-md">باز</a>
                                      <a  v-else style="background-color: #22c55e;" class=" mx-2 px-6 text-white p-2 rounded-md">بسته</a>
                                </div>
                        </div>
                        <div class="-mt-3 px-8 justify-center item max-lg:px-4 flex-col max-lg:mt-2 ">
                            <h2 class="text-gray-600 mb-2 font-bold text-[26px] px-2 transition hover:text-blue-500 max-lg:text-xl">{{ IssuesStore.singleIssues.subject }}</h2>
                            <p style="line-height: 35px;" class="main-c bg-gray-100 rounded-lg p-4 px-8 max-lg:px-4  max-lg:text-[14px] text-[16px] px-2  text-gray-500">
                                        {{ IssuesStore.singleIssues.description }}
                            </p><br>
                        </div>
                        <a :href="IssuesStore.singleIssues.assigned_attached" target="_blank" v-show="IssuesStore.singleIssues.assigned_attached" class="text-blue-500 px-8 flex items-center mt-4">
                          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.125 2.25h-4.5c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125v-9M10.125 2.25h.375a9 9 0 019 9v.375M10.125 2.25A3.375 3.375 0 0113.5 5.625v1.5c0 .621.504 1.125 1.125 1.125h1.5a3.375 3.375 0 013.375 3.375M9 15l2.25 2.25L15 12"></path>
                        </svg> 
                          <span    class="mx-1">
                            فایل سنجاق شده</span></a>
                          
                        <div class="flex justify-between">

                       
                      <div class="mb-3 max-lg:my-4 p-8 max-lg:p-4 py-5 flex justify-end ">
                        <label class="border border-blue-500  text-blue-500  hover:text-white hover:bg-blue-600  rounded ml-2 p-2 " v-if="IssuesStore.singleIssues.task" v-text=" 'تسک :'+IssuesStore.singleIssues.task_name "></label>
<label class="transition border border-purple-600 text-purple-500  hover:text-white hover:bg-purple-600 rounded ml-2 p-2 " v-if="IssuesStore.singleIssues.task" v-text="IssuesStore.singleIssues.task_importance"></label>

<label class="transition border border-yellow-500  text-yellow-500  hover:text-white hover:bg-yellow-500 rounded ml-2 p-2 " v-if="IssuesStore.singleIssues.user_role.level!=1" v-text="IssuesStore.singleIssues.user_role.skill_name"></label>

                      </div>
                      <div class="mb-3 max-lg:my-4 p-8 max-lg:p-4 py-5 flex justify-end ">

                        <a href="#replay" class="border border-blue-500  hover:text-blue-500 hover:bg-white  text-white bg-blue-600  rounded  p-2 ">  ثبت پاسخ</a>
       

                      </div>
                    
                    </div>
                    <div v-if="userStore.user.level==1 || userStore.user.id==IssuesStore.singleIssues.creator" class="border-t  border-gray-200 p-6 flex justify-end">
               <RouterLink v-if="userStore.user.id==IssuesStore.singleIssues.creator" :to="{name:'editissuess',params:{id:IssuesStore.singleIssues.id}}" href="#" class="text-sm mx-3 text-orange-400">ویرایش</RouterLink>
               <a style="cursor: pointer;" @click="deleteIssuesE (IssuesStore.singleIssues.id)" class="text-sm mx-3 text-red-400">حذف</a>

                             </div>
                </div>
                <!-- anwserssssssss -->
                <div :id="'d'+answer.id" v-for="answer in IssuesStore.singleIssues.answers" class="answer w-full shadow-sm bg-white rounded-2xl mt-6 ">
                  <div class="header w-full justify-between p-8 max-lg:p-4 flex items-center ">
                          <div class="flex flex-row items-center">
                                      <img v-if="answer.creator_avatar" :src="answer.creator_avatar" style="width: 72px;" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">
                                      <img v-else src="/assets/media/prof.png" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-gray-300" alt="">

                                      <div>
                                          <h3 class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{answer.respondent_name}}</h3>
                                         
                                          <a href="#" class="text-blue-400 text-sm max-lg:hidden">
                                            <b> تخصص:</b>
                                            <span v-if="answer.user_role.level==1" v-text="answer.user_role.level_name"></span>
                                            <span v-else v-text="answer.user_role.level_name+' ' +answer.user_role.skill_name"></span>

                                          </a>
                                         <span class="text-gray-600"> | </span>
                                          <a href="#" class="text-gray-400 text-sm" v-text="humanReadableTimeAgo(answer.updated_at)"> </a>
                                      </div>
                                  </div>
                         
                     
                  </div>
                  <div class="-mt-3 px-8 justify-center item max-lg:px-4 flex-col max-lg:mt-2 ">
                    <span v-if="answer.message_parent"  class="text-gray-500 mx-8 font-bold">   پاسخ به  <a :href="'#d'+answer.message_parent.id" class="text-blue-500"> {{answer.message_parent.respondent_name  }}</a> </span>
                      <p style="line-height: 35px;" class="main-c  rounded-lg p-4 px-8 max-lg:px-4  max-lg:text-[14px] text-[16px] px-2  text-gray-500">
{{ answer.description }}
                      </p>
                  </div>
                  <a :href="answer.assigned_attached" target="_blank" v-show="answer.assigned_attached" class="text-blue-500 px-8 flex items-center mt-4">
                          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2563eb" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.125 2.25h-4.5c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125v-9M10.125 2.25h.375a9 9 0 019 9v.375M10.125 2.25A3.375 3.375 0 0113.5 5.625v1.5c0 .621.504 1.125 1.125 1.125h1.5a3.375 3.375 0 013.375 3.375M9 15l2.25 2.25L15 12"></path>
                        </svg> 
                          <span    class="mx-1">
                            فایل سنجاق شده</span>
                        </a>
                    
                  <div class="flex justify-between">

                 
                <div class="mb-3 max-lg:my-4 p-8 max-lg:p-4 py-5 flex justify-end ">

            

                </div>
                <div class="mb-3 max-lg:my-4 p-8 max-lg:p-4 py-5 flex justify-end ">

                  <a href="#replay" @click="message.message_parent=answer" class="border border-blue-500  hover:text-blue-500 hover:bg-white  text-white bg-blue-600  rounded  p-2 ">  ثبت پاسخ</a>
 

                </div>
        
              </div>
              <div v-if="userStore.user.level==1 || userStore.user.id==answer.respondent" class="border-t mt-3 border-gray-200 p-8 flex justify-end">
               <RouterLink v-if="userStore.user.id==answer.respondent" :to="{name:'editmessage',params:{messageid:answer.id,id:IssuesStore.singleIssues.id}}" href="#" class="text-sm mx-3 text-orange-400">ویرایش</RouterLink>
               <a style="cursor: pointer;" @click="deleteMessage(answer.id)" class="text-sm mx-3 text-red-400">حذف</a>

                             </div>
          </div>
            </div>
        </section>

        <section v-if="IssuesStore.singleIssues.status==1">
          <div id="replay" class="row my-4 max-lg:mt-4  w-[90%] flex flex-col  mx-auto justify-center max-lg:w-full max-lg:px-4">
              <div class="questions w-full shadow-sm bg-white rounded-2xl mt-6 ">
                      <div class="header w-full justify-between p-8 max-lg:p-4 flex items-center ">
                              <div class="flex flex-row items-center">
                                          <img v-if="userStore.user.avatar" :src="userStore.user.avatar" style="width: 72px;" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-green-500" alt="">
                                          <img v-else src="/assets/media/prof.png" class="h-[72px] max-lg:h-14 transition hover:border-blue-500 ml-4 rounded-full border-[3px] border-green-500" alt="">

                                          <div>
                                            <h3 v-if="userStore.user.firstname" class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{userStore.user.firstname+' '+userStore.user.lastname}}</h3>
                                            <h3 v-else class="text-gray-600 text-[22px] max-lg:text-[18px] font-bold">{{'بدون نام'+ "|"+userStore.user.email}}</h3>
                                              <a href="#" class="text-blue-400 text-sm"> 
                                                <b>تخصص: </b>
                                                  <span v-if="userStore.user.current_project">
                                                    <span v-if="userStore.user.level==1">مدیر پروژه</span>
    <span v-else-if="userStore.user.level==2" style="width: auto;"> کارمند ارشد {{ userStore.user.rollname }} </span>
        
    <span v-else="userStore.user.level==2">کارمند {{ userStore.user.rollname }}  </span>
                                                  </span>
                                                {{  }}
                                              </a>
                                          </div>
                                      </div>
                             
                          
                      </div>
                      <div class="max-lg:p-5">
                      <div class="max-lg:w-full  w-5/6 mx-auto bg-blue-100 p-4 rounded-md border border-blue-500 flex justify-center flex-col">
                          <b class="text-blue-600">قبل از ارسال پرسش دقت کنید</b>
                          
                          <p class="text-blue-500 mt-2">
1- شما مجاز به آپلود فقط یک فایل هستید پس لطفا  در صورتی که بیش از چندفایل دارید لطفا آن ها را zip کرده و بارگذاری نمایید.
                          </p>
                      </div>
                    

                      </div>
                      <form   @submit.prevent="send" class="mt-4 max-lg:mt-1 p-8 w-full max-lg:p-6">

               
                          <h2 class="p-4" style="font-size: 18px;" v-if="message.message_parent">شما در حال پاسخ به 
                            <a :href="'#d'+message.message_parent.id" class="text-blue-500">{{ message.message_parent.respondent_name }}</a>
                            هستید
                          <span style="cursor: pointer;" @click="message.message_parent=null" class="text-red-500">(حذف)</span>
                          </h2>

                          <div class="flex justify-center p-2">
                            <textarea required v-model="message.description" rows="5" id="" class="w-full  mt-4 bg-[#f3f3f3] border  rounded-lg border-gray-300 focus:border-blue-500 p-4 text-gray-600 outline-blue-500" placeholder="چیزی برای نوشتن وارد کنید"></textarea>

                          </div>
                          <div class="w-full mt-3 mb-6 px-2">
                            <label class="block font-bold text-2xl max-lg:text-xl  text-gray-700 dark:text-white mb-4" for="default_size"> آپلود مستندات ( اختیاری)</label>
                            <input @change="handleFileUpload"  class="block w-full mb-5 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer p-3 bg-[#f3f3f3] dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="default_size" type="file">                            </div>
                          <div class="w-full flex justify-end">
                            <button
                            :class="[
                                'flex items-center submit justify-center bg-blue-500 hover:bg-blue-400 justify-between  px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform rounded-lg focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50',
                                sendloading ? ' disabled' : ''
                            ]" :disabled="sendloading"
                         >ثبت پاسخ</button>
                          </div>
                      </form>

                  
                  
              </div>
          </div>
      </section>

</div>
</template>

<style>
#openBtn:hover{
color: #22c55e;
}
</style>

<script setup>
import { useIssuesStore } from '@/stores/IssuesStore';
import { useUserStore } from '@/stores/user';
import { onMounted,reactive,ref } from 'vue';
import humanReadableTimeAgo from '@/utils/dateLog';
import swswalDel from "@/utils/swal.js"

import { useRoute } from 'vue-router';
import router from '@/router';
const loading=ref(false)
const userStore=useUserStore()
const IssuesStore=useIssuesStore()
const route=useRoute()

const sendloading=ref(false)

const message=reactive({
  id:'',
  projectID:'',
  description:'',
  message_parent:''
})

onMounted(async()=>{

    await IssuesStore.getSingleIssues(route.params.id,userStore.user.current_project)
    loading.value=true
})

async function closeQuestion(st){
    await IssuesStore.closeOpenIssues(st,route.params.id,userStore.user.current_project)
}
function melength(x){
    if(x[0]){  
    return x.length
}
return 0
}
let av=null
  function handleFileUpload(event) {
    av = event.target.files[0];
  
    }


async function send(){
    if (!sendloading.value) {
        sendloading.value=true
        message.projectID=userStore.user.current_project
        message.id=route.params.id
        await IssuesStore.addMessage(message,av).then((res)=>{
     
          message.description=""
          message.message_parent=null
          av=""

        })
         
        sendloading.value=false
  
    }
  }
  async function deleteMessage(id){
  await  swswalDel().then((res)=>{
    if (res.isConfirmed){
         IssuesStore.deleteMessage(userStore.user.current_project,route.params.id,id).then((res)=>{})
    }
  })

}
async function deleteIssuesE(id){
  await  swswalDel().then((res)=>{
    if (res.isConfirmed){
         IssuesStore.deleteIssues(id,userStore.user.current_project).then((res)=>{}).catch((er)=>{
          console.log(er)
         })
         router.push('/discuss/')
    }
  })

}
</script>