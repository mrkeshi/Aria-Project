<template>
        <header class="relative ">
          <!-- Top Navbar-->
          <div class="header-top px-4 lg:mt-12 md:mt-8 max-md:mt-3 bg-white  rounded-3xl ">
            <div class=" mx-sm:px-7 lg:w-5/6 w-full mx-auto ">
              <div class="flex justify-between h-28 max-lg:h-24 max-md:h-20 items-center  ">
                 
                <a v-if="projectname" href="#" class="text-gray-600 text-2xl font-bold max-lg:text-xl">
                    پروژه  : {{projectname}} 
                    </a>
                    <a v-else href="#" class="text-blue-700 text-2xl font-bold max-lg:text-xl">
                     بدون پروژه
                    </a>
    
    <!-- navbar top contains 2 icon!! -->
    
                <div class="icon-top  ">
    
                  <ul>
                    <div class=" flex relative   ">
    
    
                       
                      <li class="person_manage_icon h-auto w-auto  " style="z-index: 0;">
                        <a href="#">
                          <div class="flex items-center mx-1">
                            <div class="w-14 h-14 rounded-full bg-gray-300 border-2   border-blue-600 text-black-700 flex justify-center items-center hover:text-white hover:bg-black-700 ease-in transition">
                             <img v-if="myuser.avatar" :src="myuser.avatar" class="rounded-full w-14 h-14" alt="">
                             <img v-else class="rounded-full" src="/assets/media/prof.png" alt="">
                            </div>
    
                          </div>
    
                        </a>
                      </li>
                      <div id="showusermanage" class="bg-white z-50 h-auto w-[180px] pointer-events-none opacity-0 ease-linear transition-opacity appearance-none top-12 -left-12 max-lg:-left-3 shadow-md mt-4 absolute " style="z-index: 99;">
                        <ul class="">
                          <li class="py-3 px-4 pt-5 hover:bg-gray-300 text-mxl text-gray-700">
                            <RouterLink :to="{name:'dashbaord'}" class="flex w-full h-full">
                             
                              داشبورد
    
                            </RouterLink></li>
                        
                          <li class="py-3 px-4 text-mxl hover:bg-gray-300 text-gray-700">
                            <RouterLink :to="{name:'profile'}" class="flex w-full h-full">
                              پروفایل
                            </RouterLink>
                        </li>
                          <li @click="logoutEvent" class="py-3 px-4 pb-5 text-mxl hover:bg-gray-300 text-red-500">
                            <a href="#" class="flex w-full h-full">
    
                               خروج
                            </a></li>
    
                        </ul>
    
                      </div>
    
    
                    </div>
                  </ul>
    
    
    
                </div>
    
              </div>
            </div>
          </div>
          <!-- End Top Navbar And Start Bottom Navbar -->
    
      <div class="w-5/6 SiteMenu bg-gray-300 rounded-b-3xl mx-auto  mobile_navbar lg:static max-lg:h-[100vh] max-lg:hidden " >
    
      <nav class="">
        <ul class="">
          <div class="flex  text-black-500 text-mxl justify-center py-5 lg:h-[76px]  items-center  ">
    
            <div style="margin-right: -8px !important;width: 95%; " class="relative max-lg:mt-8 max-lg:mb-3 lg:hidden  ">
              <div class="absolute inset-y-0 left-3 top-3 flex items-center pointer-events-none">
                <svg aria-hidden="true" class="w-4 h-4 text-black-700 " fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
              </div>
              <input type="search" class="  p-3 w-full h-11 transition ease-linear text-sm bg-gray-300  text-black-700 border border-gray-300 rounded-2xl  focus-visible:outline-none focus:border-gray-500 relative" placeholder="جست و جو کنید" required="">
            </div>
              <hr class="text-black-500 w-full -mr-3 my-4 lg:hidden">
            <div class="flex text-gray-600 text-mxl justify-center mx-0 lg:h-[76px] items-center h-full overflow-y-auto scrollbar scrollbar-thumb-gold-100 scrollbar-track-gray-500 scrollbar-w-[3px] overflow-x-hidden scrollbar-track-rounded-md scrollbar-thumb-rounded-lg  max-lg:w-[95%]  max-lg:h-[screen]" style="margin-right: 0">
    
          
              <li class="xl:mx-8 mx-5 hover:opacity-75 flex justify-center items-end">
            
              <RouterLink :to="{name:'dashbaord'}" class="flex items-end">
           
                داشبورد
    
              </RouterLink>
            </li>
            <li class="xl:mx-8 mx-6 hover:opacity-75 ">
            
              <RouterLink :to="{name:'project'}"  class="flex items-end">
                مدیریت پروژه</RouterLink>
            </li>
            <li class="xl:mx-8 mx-6 hover:opacity-75 flex items-end">
            
              <RouterLink :to="{name:'task'}" href="blog.html" class="flex items-end">
            تسک</RouterLink>
            </li>
            <li class="xl:mx-8 mx-6 hover:opacity-75 flex items-end">
             
              <RouterLink :to="{name:'report'}" href="search.html" class="flex items-end"> 
   
              مانیتورینگ
              </RouterLink></li>
              <li class="xl:mx-8 mx-6 hover:opacity-75 flex items-end">
                
              <RouterLink :to="{name:'metting'}" href="contact.html" class="flex items-end">
    
             جلسه
              </RouterLink>
            </li>
            <li class="xl:mx-8 mx-6 hover:opacity-75 flex items-end">
                
              <RouterLink :to="{name:'issuess'}" href="contact.html" class="flex items-end">  
             پرسش پاسخ
              </RouterLink>
            </li>
    
          </div>
          </div>
        </ul>
      </nav>
    </div>
    
         
        </header>

</template>

<script setup>
    import { RouterLink } from 'vue-router';
    import { singleProject } from '@/services/projects';
import { useAuthStore } from '@/stores/auth';
import { useUserStore } from '@/stores/user';
import { onMounted, ref, watch } from 'vue';
import { reactive } from 'vue';
import router from '@/router';
const projectname=ref(null)

async function getprojectName(){
  if (user.user.current_project != null) {
     
     await singleProject(auth.user.access,user.user.current_project).then((response)=>{
           console.log("RESPPONSE",response.data.title)
       projectname.value=response.data.title
     });
   } 
       else {
     projectname.value = null;
   }
}
onMounted(async ()=>{
 await  getprojectName()

  let Boxes=new MangeBoxDropDown()
    window.addEventListener('click', (event) => {
      if(!Boxes.personBox.contains(event.target) && event.target.contains(Boxes.filterBody)){
        Boxes.closePersonBox()
      }
     
    })
})

const user=useUserStore()
const auth=useAuthStore()
async function logoutEvent(){
    await auth.logoutAction()
    router.push('/login');

}

watch(
  async () => user.user.current_project, 
  async (newValue) => {  

    if (user.user.current_project != null) {

      await singleProject(auth.user.access,user.user.current_project).then((response)=>{
      
        projectname.value=response.data.title
      
      });
    } else {
      projectname.value = null;
    }

  },
  { deep: true }
);
watch(
  async () => user.projectname, 
  async (newValue) => {  

    if (user.user.current_project != null) {

      await singleProject(auth.user.access,user.user.current_project).then((response)=>{
      
        projectname.value=response.data.title
      
      });
    } else {
      projectname.value = null;
    }

  },
  { deep: true }
);


// my script Code




class MangeBoxDropDown{
  filterBody = document.getElementById('filter-overflow');
    //  icon
    personBoxIcon=document.querySelector('.person_manage_icon')
    cardBoxIcon=document.querySelector('.card_manage_icon')
    // boxes
    personBox= document.getElementById('showusermanage')
    cardBox= document.getElementById('showcardmanage')
    // 
    constructor(){
        if(document.querySelector('.person_manage_icon')){
            this.personBoxIcon.addEventListener('click',()=>{
                if(this.personBox.classList.contains('showusermanage')){
              
                 this.closePersonBox()
                }else{
                 this.openPersonBox()
                } 
         })
        }
     
        if(document.querySelector('.card_manage_icon')){
                this.cardBoxIcon.addEventListener('click',()=>{
            
                    if(this.cardBox.classList.contains('showcarmanage')){
                        this.closeCardBox()
                    }else{
                        this.openCardBox()
                    }
                
            })
            }
      
    }
    openPersonBox(){
        this.personBoxIcon.style.zIndex=99
        this.personBox.style.zIndex=99
        this.personBox.classList.add('showusermanage')
        this.filterBody.classList.remove('hidden')
    }
    openCardBox(){
        this.cardBoxIcon.style.zIndex=99
        this.cardBox.style.zIndex=99
        this.cardBox.classList.add('showcarmanage')
        this.filterBody.classList.remove('hidden')
    }
    closePersonBox(){
        this.personBoxIcon.style.zIndex=0
        this.personBox.style.zIndex=0
        this.personBox.classList.remove('showusermanage')
        this.filterBody.classList.add('hidden')
    }
    closeCardBox(){
        this.cardBoxIcon.style.zIndex=0
        this.cardBox.style.zIndex=0
        this.cardBox.classList.remove('showcarmanage')
        this.filterBody.classList.add('hidden')

    }
}
      
 

 
const myuser=reactive({
             avatar: null,
            id: null,
            email: null,
            current_project:null,
            firstname:null,
            lastname:null,
            level:null,
            rollname:''
})
const updateMyUser = () => {
    Object.assign(myuser, { ...user.user });
};

onMounted(async ()=>{
       await user.getDetail()
   updateMyUser();

    })
    watch(() => user.user, (newValue) => {
    updateMyUser(); 
}, { deep: true });
watch(() => user.user.current_project, (newValue) => {
    
    user.getLeveAction(user.user.current_project)
}, { deep: true });

</script>

<style>

</style>