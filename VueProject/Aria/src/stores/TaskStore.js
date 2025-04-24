import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
import { addTask, deleteTask, editTask, getDetailTask,updateTaskAdmin,ShowTasksAdmin,ScoreTaskAdmin, ShowTasksFilter } from "@/services/TaskServices";
const toast=useToast(

)
import { useAuthStore } from "./auth";
import router from "@/router";
const auth=useAuthStore()
export const useTaskStore=defineStore({
    id:'task',

    state: () => ({
    
        task:{},
        tasks:[],

    }),
    actions:{
    
       
        async ShowallTaskAction(){
          
            console.log(auth.user)
            return await ShowTasksAdmin(auth.user.access).then((res)=>{

                this.tasks=res.data
            }).catch((er)=>{
                console.log(er)
            })
        },
        async ShowallTaskFilterAction(id){
          
            console.log(auth.user)
            return await ShowTasksFilter(auth.user.access,id).then((res)=>{
                console.log(res)
                this.tasks=res.data
            }).catch((er)=>{
                console.log(er)
            })
        },
        async SingleTaskAction(id){
           return await getDetailTask(auth.user.access,id).then((response)=>{
            this.task=response.data
           })
        },
        async deltask(id){
            return await deleteTask(auth.user.access,id).then((response)=>{
                console.log(response)
                toast.success("تسک با موفقیت حذف شد.")
            }).catch((er)=>{
                toast.warning("خطا در حذف تسک")
            })
        },
        async addtaskAction(info,av){
            return await addTask(auth.user.access,info,av).then((Response)=>{
                toast.success("تسک با موفقیت ساخته شد")
                router.push('/dashboard/tasks')
            }).catch((er)=>{
                console.log(er);
                toast.warning("خطا در ساخت تسک لطفا ورودی ها را کنترل کنید. ")
            })
        },
        async edittaskadmin(info,id,av){
        
            return await updateTaskAdmin(auth.user.access,info,id,av).then((res)=>{
                toast.info("تسک با موفقیت ویرایش شد")
                router.push("/dashboard/tasks")

            }).catch((er)=>{
                console.log(er)
                toast.warning("خطا در بروزرسانی تسک")

            })
        },
        async scoretaskadmin(info,id){
        
            return await ScoreTaskAdmin(auth.user.access,this.task,id).then((res)=>{
                toast.info("امتیاز و بازخورد با موفقیت ثبت شد")
                router.push("/dashboard/tasks")

            }).catch((er)=>{
                console.log(er)
                toast.warning("خطا در بروزرسانی تسک")

            })
        },
        async updatetaskuser(info,id,av){
           return await editTask(auth.user.access,info,id,av).then((response)=>{
            toast.success("تسک با موفقیت بروزرسانی شد")
            router.push("/dashboard/tasks")
           }).catch((er)=>{
            console.log(er)
            toast.warning("خطا در بروزرسانی تسک")
           })
        }
    },
    
})