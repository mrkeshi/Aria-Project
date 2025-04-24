import axios from "@/utils/axios";

 const getDetailTask= (token,id)=>{
    
    return axios.get(`tasks/UserTasks/${id}/`,{
        headers: {
            Authorization: `JWT ${token}`
        }
    })
}
const updateTaskAdmin=(token,info,id,file)=>{


    return axios.put(`tasks/ManageTasks/${id}/`,{
        "attached":file,
        "title": info.title,
        "description": info.description,
        "finished_at": info.finished_at,
        "importance": info.importance,
        "assigned":info.assigned,
        "project": info.project,
        "progress": info.progress,
        "owner_note":info.owner_note,
        "rate":info.rate
    },   {
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}


const ScoreTaskAdmin=(token,info,id)=>{


    return axios.put(`tasks/ManageTasks/${id}/`,{
        "title": info.title,
        "description": info.description,
        "finished_at": info.finished_at,
        "importance": info.importance,
        "assigned":info.assigned,
        "project": info.project,
        "owner_note":info.owner_note,
        "rate":info.rate
    },   {
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}
const getUserWithSkilService=(token,id)=>{4
   
    return axios.get(`tasks/users-with-skill/${id}`, {
        headers: {
            Authorization: `JWT ${token}`,
        }
    })
}
const addTask=(token,info,file)=>{


    return axios.post("tasks/ManagerManageTasks/",{
        "attached":file,
        "title": info.title,
        "description": info.description,
        "finished_at": info.finished_at,
        "importance": info.importance,
        "assigned":info.assigned,
        "project": info.project,
        
    },   {
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}


const ShowTasksAdmin=(token)=>{
  
    return axios.get(`tasks/UserTasks/`,{
        headers: {
            Authorization:`JWT ${token}`,
        }
    })
}

const ShowTasksFilter=(token,id)=>{
  
    return axios.get(`tasks/ManagerManageTasks?assigned=${id}`,{
        headers: {
            Authorization:`JWT ${token}`,
        }
    })
}
const getNameAssigned=(token,project,id)=>{
    return axios.get(`auth/api/user/${id}/`,{
        headers: {
            Authorization:`JWT ${token}`,
        }  
    })
}
const editTask=(token,progress,id,av)=>{
    let done=false
    if(progress==100){
        done=true
    }
    return axios.put(`/tasks/UserTasks/${id}/`,{
        "progress":progress,
        "assigned_attached":av,
        "done":done
    },{
        headers: {
              "Content-Type": "multipart/form-data",
            Authorization: `JWT ${token}`,

        }
    })
}
const deleteTask=(token,id)=>{
    return axios.delete(`tasks/ManageTasks/${id}/`, {
        headers: {
            Authorization: `JWT ${token}`,
        }
    })
}
export {editTask,getNameAssigned,ShowTasksFilter,ShowTasksAdmin,addTask,updateTaskAdmin,getDetailTask,deleteTask,getUserWithSkilService,ScoreTaskAdmin}