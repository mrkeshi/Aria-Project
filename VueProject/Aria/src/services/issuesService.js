import axios from "@/utils/axios";

 const getDetailIsSerivce= (token,id,projectID)=>{
    
    return axios.get(`http://127.0.0.1:8000/workspace/project/${projectID}/questions/${id}/`,{
        headers: {
            Authorization: `JWT ${token}`
        }
    })
}
const updateIsService=(token,info,file,id,projectID)=>{

  
    return axios.put(`http://127.0.0.1:8000/workspace/project/${projectID}/questions/${id}/`,{
        "subject":info.title,
        "assigned_attached": file,
        "description": info.description,
        "task": info.task,
    },{
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}


const closeOpenIsService=(info,token,status,id,projectID)=>{
    return axios.put(`http://127.0.0.1:8000/workspace/project/${projectID}/questions/${id}/`,{
        "status":status,
        "subject":info.subject,
        "description": info.description,
    },{
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}
const getAllissuesService=(token,id)=>{
   
    return axios.get(`http://127.0.0.1:8000/workspace/project/${id}/questions/`,{
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
const getAMyissuesService=(token,id,creator)=>{
   
    return axios.get(`http://127.0.0.1:8000/workspace/project/${id}/questions?creator=${creator}`,{
        headers: {
            Authorization: `JWT ${token}`,
          
        }
    })
}
const addissuesService=(token,info,file)=>{


    return axios.post(`http://127.0.0.1:8000/workspace/project/${info.id}/questions/`,{
        "subject":info.title,
        "assigned_attached": file,
        "description": info.description,
        "task": info.task,
        
    },{
        headers: {
            Authorization: `JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}
const deleteissuesService=(token,id,projectID)=>{
   
    return axios.delete(`http://127.0.0.1:8000/workspace/project/${projectID}/questions/${id}/`,{
        headers: {
            Authorization: `JWT ${token}`
        }
    })
}

const showMessageService=(token,id,projectID,messageID)=>{
  
    return axios.get(`workspace/project/${projectID}/questions/${id}/answers/${messageID}/`,{
        headers: {
            Authorization:`JWT ${token}`,
        }
    })
}


const deleteMessageService=(token,projectID,id,messageID)=>{
    return axios.delete(`/workspace/project/${projectID}/questions/${id}/answers/${messageID}/`, {
        headers: {
            Authorization: `JWT ${token}`,
        }
    })
}


const editMessageService=(token,id,projectID,messageID,info,av)=>{
    let x=0;
    if(info.message_parent){
        x=info.message_parent.id
    }else{
        x=info.message_parent
    }
    return axios.put(`workspace/project/${projectID}/questions/${id}/answers/${messageID}/`,{
            'description':info.description,
            'assigned_attached':av,
            'message_parent':x,
    },{
        headers: {
            Authorization:`JWT ${token}`,
            "Content-Type": "multipart/form-data"
        }
    })
}
const addMessageService=(token,info,av)=>{
    let x=0;
    if(info.message_parent){
        x=info.message_parent.id
    }else{
        x=info.message_parent
    }
   

    return axios.post(`workspace/project/${info.projectID}/questions/${info.id}/answers/`,
        {
            'message_parent':x,
            'description':info.description,
            'assigned_attached':av
        }, {
            headers: {
                 Authorization: `JWT ${token}`,
                 "Content-Type": "multipart/form-data"
             }
            }
            )
}

export {editMessageService,getAMyissuesService,addMessageService,deleteissuesService,deleteMessageService,showMessageService,addissuesService,getAllissuesService,closeOpenIsService,updateIsService,getDetailIsSerivce}