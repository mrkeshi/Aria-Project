import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
import { addUser, deleteuserService, getDetailuser, getLevel, updateProfile } from "@/services/user";
const toast=useToast(

)
import { useAuthStore } from "./auth";
import router from "@/router";
import { getProjects } from "@/services/projects";
const auth=useAuthStore()
export const useUserStore=defineStore({
    id:'user',
    state: () => ({
        user: {
            avatar: null,
            id: null,
            email: null,
            current_project:null,
            firstname:null,
            lastname:null,
            level:null,
            rollname:'',
            isactive:null
        },
        returnUrl: null,
        projectname:null,

    }),
    actions:{
    
        async getDetail(){
               await getDetailuser(auth.user.access).then((response)=>{
                console.log(auth.user.access)

                    if(!response.data.current_project){

                        this.user.level=0
                    }else{
                        this.user.current_project=response.data.current_project
                    }
                 
                    const data=response.data
                    this.user.firstname=data.first_name
                    this.user.lastname=data.last_name
                    this.user.email=data.email
                    this.user.avatar=data.avatar
                    this.user.id=data.id
                    this.user.isactive=data.is_active
               
                     getLeveAction(data.id)
                }).catch((er)=>er)
     
        },
        async getLeveAction(id){
            await getLevel(id,auth.user.access).then((response)=>{
                console.log(response)
                this.user.level=response.data.level
                this.user.rollname=response.data.skill
            }).catch((er)=>{
                this.user.level=0
            })
        },
        async updateProfileAction(info,avatar){
            updateProfile(auth.user.access,info,auth.user.email,avatar).then((el)=>{
                this.getDetail(auth.user.access)
                toast.success("تغییرات با موفقیت ایجاد شد")
            }).catch((error)=>{
                let errordata=error.response.data 
                console.log(errordata)
                Object.entries(errordata).forEach(([key, messages]) => {
                    toast.error(` ${key}: ${messages}`);
                })
            })
            
        },
        async add(token,info,id){

        return  await  addUser(token,info,id).then((data)=>{
                toast.success("کاربر با موفقیت به پروژه اضافه شد")
                router.push("/dashboard/users/")
            }).catch((er)=>{
                toast.error("خطا در دعوت کاربر به پروژه")
                console.log("errrrrrrrror:",er)
                if(er.response.data.message){
                    toast.error(er.response.data.message)
                }
                

            })
        },
        async deleteUser(id,userId){
            await deleteuserService(auth.user.access,id,userId).then((res)=>{
                
                toast.success(`کاربر جاری با موفقیت از پروژه حذف شد.`)
            }).catch((er)=>{
                console.log(er)
                toast.warning("شما مجاز به حذف این کاربر نیستید.")
            })
        }
        
    },
    
})