import{Q as S}from"./TouchPan.54530d87.js";import{_ as E,r,c as g,l as k,v as I,n as t,d as s,a8 as f,A as C,q as i,t as L,u as M,aM as V,bn as w,M as b,a9 as U,b as B,bo as F,bb as $,aa as N,ab as O}from"./index.c822f9b0.js";import{Q as A}from"./QSelect.30415dcc.js";import{Q as K}from"./QScrollArea.fcae44dc.js";import{Q as T}from"./QForm.5279d460.js";import{u as j}from"./axios.2c985eff.js";import{u as R,Q as z}from"./QSpinnerFacebook.173d39e4.js";const p=n=>(N("data-v-009d1e8d"),n=n(),O(),n),G=p(()=>i("div",{class:"text-h6 text-bold",style:{color:"#123499"}}," Edit Commission Details ",-1)),H={class:"text-bold"},J={class:"text-green"},W=p(()=>i("div",{class:"text-bold q-mt-md"},"Commission Level",-1)),X=p(()=>i("div",{class:"text-bold q-mt-md"},"Commission Pay Date",-1)),Y=p(()=>i("div",{class:"text-bold q-mt-md"},"Comments",-1)),Z={__name:"editCommissionDetailsModal",props:{showEditCommissionPopup:{type:Boolean,required:!0,default:!1},closeEditCommissionPopup:{type:Function,required:!0},selectedData:{type:Object,required:!0}},setup(n){const l=n,D=j(),c=r("One"),Q=r(["One","Two","Three","Four"]),d=r(""),m=r(""),u=R(),v=g({get:()=>l.showEditCommissionPopup,set:()=>l.closeEditCommissionPopup()}),x=g(()=>{let a=_(d.value),e=_(m.value);return!a||!e}),P=()=>{u.loading.show({spinner:z,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},q=()=>{u.loading.hide()},y=a=>{l.closeEditCommissionPopup(a)},_=a=>a.trim().length>2,h=a=>{P();let e={commissionStatus:a,commissionLevel:c.value,commissionPayDate:d.value,comments:m.value,customerNumber:l.selectedData.customer_number};D.updateCommissionDetails(e).then(o=>{u.notify({message:"Commission Details Updated Successfully!!!",type:"positive",position:"top"}),y(!0)}).catch(o=>{u.notify({message:"Error in updating Commission details. Please contact your admin!!!",type:"negative",position:"top"})}).finally(()=>{q()})};return(a,e)=>(k(),I($,{modelValue:b(v),"onUpdate:modelValue":e[5]||(e[5]=o=>B(v)?v.value=o:null),persistent:"",onKeydown:F(y,["esc"])},{default:t(()=>[s(U,{class:"commission-modal q-pl-sm"},{default:t(()=>[s(f,{class:"row items-center"},{default:t(()=>[G,s(S),s(C,{icon:"close",flat:"",round:"",onClick:y})]),_:1}),s(T,null,{default:t(()=>[s(K,{style:{height:"calc(58vh - 170px)"}},{default:t(()=>[s(f,null,{default:t(()=>[i("div",H,[L(" Customer - "),i("span",J,M(`${l.selectedData.customer_name} - ${l.selectedData.customer_number}`),1)]),W,s(A,{class:"q-mt-sm",style:{width:"250px"},filled:"",dense:"",modelValue:c.value,"onUpdate:modelValue":e[0]||(e[0]=o=>c.value=o),options:Q.value},null,8,["modelValue","options"]),X,s(V,{modelValue:d.value,"onUpdate:modelValue":e[1]||(e[1]=o=>d.value=o),style:{"max-width":"250px"},outlined:"",dense:"",autofocus:"",type:"date"},null,8,["modelValue"]),Y,s(V,{modelValue:m.value,"onUpdate:modelValue":e[2]||(e[2]=o=>m.value=o),type:"textarea",style:{width:"250px"},outlined:"",dense:"",autofocus:"",rows:"6","input-class":"textarea-input",placeholder:"Payment Comments",rules:[o=>_(o)||"Field is required!!!"]},null,8,["modelValue","rules"])]),_:1})]),_:1}),s(f,{class:"row justify-end"},{default:t(()=>[s(w,{class:"q-px-none"},{default:t(()=>[s(C,{class:"q-mr-sm",unelevated:"",color:"primary",label:"Payment Issue",disable:b(x),onClick:e[3]||(e[3]=o=>h("paymentIssue")),"no-caps":""},null,8,["disable"])]),_:1}),s(w,{class:"q-px-none"},{default:t(()=>[s(C,{unelevated:"",color:"primary",label:"Paid",disable:b(x),onClick:e[4]||(e[4]=o=>h("paid")),"no-caps":""},null,8,["disable"])]),_:1})]),_:1})]),_:1})]),_:1})]),_:1},8,["modelValue","onKeydown"]))}};var ne=E(Z,[["__scopeId","data-v-009d1e8d"]]);export{ne as e};
