import { defineStore } from "pinia";
import { editProject, getProjects, setProject, singleProject,setCurrentProject, deleteproj, getUserInProject, UpdateRole } from "@/services/projects";
import { useToast } from "vue-toastification";
import router from "@/router";
import { useUserStore } from "./user";
import { useReportStore } from "./Reporting";
const toast = useToast();

export const useProjectStore = defineStore({
    id: 'projects',
    state: () => ({
        projects: [],
        single:{
            title:'',
            description:'',
            Progress:0
        },
        myproject:{
            title:'',
            id:''
        },
        role:{}
        
    }),

    actions: {
        async getprojects(token) {
            try {
                const response = await getProjects(token);
                this.projects = response;
           
            } catch (error) {
                this.projects = {};
                toast.error("هیچ پروژه ای جهت نمایش وجود ندارد"); 
            }
        },
        async addProject(title,description,token){
            setProject(title,description,token).then((data)=>{
                this.setProjCurrent(token,data.data.id)
                toast.success("پروژه با موفقیت ساخته شد")
                router.push('/dashboard/project')
            }).catch((error)=>{
                toast.error("خطا در ساخت پروژه")
            })
        },
        async setProjCurrent(token,id){
            const usr=useUserStore()
            setCurrentProject(token,id).then((data)=>{
                usr.user.current_project=id

                toast.success("با موفقیت به پروژه مد نظر سوئیچ شدید .")
                router.push('/dashboard/')

            }).catch((error)=>{
                console.log(error)
                toast.error("خطا")
            })
        },
        async deleteprojACtion(token,current,id){
            deleteproj(token,id).then((data)=>{
                toast.success("پروژه مد نظر با موفقیت حذف شد ")
                if(current==id){
                    const usr=useUserStore()
                    usr.user.current_project=null
                    this.getprojects(token)
                    const re=useReportStore()
                 
                    router.push('/dashboard')

                }else{
                    this.getprojects(token)
                }
                console.log("projects",this.projects)
             

            }).catch((error)=>{
                console.log(error)
                toast.error("خطا در حذف پروژه")
            })
        },
        async editProject(title,description,token,id){
          const user=useUserStore()
            editProject(title,description,token,id).then((data)=>{
                toast.success("پروژه با موفقیت ویرایش شد")

                if(user.user.current_project==id){
                    user.user.current_project=id
                    user.projectname=data.data.title
                }
                router.push('/dashboard/project/')
            }).catch((error)=>{
                console.log("errror:",error)
                toast.error("خطا در ویرایش پروژه")
            })
        },
        async getSingle(token,id){
    
          await singleProject(token,id).then((data)=>{
            this.single.title=data.data.title
            this.single.description=data.data.description
          
            this.single.Progress=data.data.average_rate
                    }).catch((error)=>{
                console.log(error)
                toast.error("شما به این صفحه دسترسی ندارید.")
                router.push("/dashboard/project")
            })
        },
        async getRole(token,projectId,roleId){
            await getUserInProject(token,projectId,roleId).then((res)=>{
         
               this.role=res.data
            }).catch((er)=>{
                console.log(er)
            })
        },
        async editRole(token,projectId,roleId,info){
                await UpdateRole(token,projectId,roleId,info).then((res)=>{
                    toast.success("نقش کاربر باموفقیت ویرایش شد")
                    router.push('/dashboard/users/')
                }).catch((er)=>{
                    console.log(er)
                })
        }
    }
})
