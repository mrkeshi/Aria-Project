import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
import { useAuthStore } from "./auth";
import { createSkill, deleteSkill, editskill } from "@/services/skil";
import router from "@/router";

export const useSkillStore = defineStore({
    id: 'skill',
    state: () => ({
        skils: {
        },
        returnUrl: null,

    }),
    actions: {
        async create(info) {
            
            const auth = useAuthStore();
            const toast = useToast();  

            if (!auth.user || !auth.user.access) {
                toast.error("کاربر احراز هویت نشده است");
                return;
            }

            try {
                await createSkill(auth.user.access, info);
                toast.success("فیلد با موفقیت ساخته شد");
                router.push("/dashboard/skill/");
            } catch (er) {
                toast.error("خطا در ساخت فیلد");
                console.log(er);
            }
        },
        async delete(id){
            const auth = useAuthStore();
            const toast = useToast(); 
            await deleteSkill(auth.user.access,id).then((response)=>{
                    toast.success("فیلد با موفقیت حذف شد")
                    router.push('/dashboard/users');
    
            }).catch((er)=>{
                toast.warning("خطا در حذف فیلد")
            })
        },
        async edit(id,info){
            const auth = useAuthStore();
            const toast = useToast(); 
            await editskill(auth.user.access,id,info).then((data)=>{
                toast.success("با موفقیت ویرایش شد")
                router.push('/dashboard/skill');
            }).catch((err)=>{
                toast.warning("خطا در ویرایش")
                console.log("errror",err)
            })
        }
    },
   
});