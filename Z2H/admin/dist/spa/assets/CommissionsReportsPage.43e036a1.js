import{_ as z,r as a,c as j,l as T,m as Y,q as n,d as l,aM as S,M as O,A as D,n as o,v as N,x as R,F as G,Q as k,t as m,u as i,aa as H,ab as J}from"./index.c822f9b0.js";import{Q as x,j as r}from"./QSelect.30415dcc.js";import{Q as u}from"./QTd.97012c36.js";import{Q as K}from"./QTable.c6a0c61c.js";import{u as W,Q as X}from"./QSpinnerFacebook.173d39e4.js";import{u as Z}from"./axios.2c985eff.js";import{e as ee}from"./exportToExcel.602deb22.js";import{e as oe}from"./editCommissionDetailsModal.63ac065a.js";import"./format.65b096e9.js";import"./QList.df78d7a2.js";import"./QMarkupTable.64b2e607.js";import"./TouchPan.54530d87.js";import"./touch.3df10340.js";import"./QScrollArea.fcae44dc.js";import"./QResizeObserver.230413fd.js";import"./QScrollObserver.88406e47.js";import"./QForm.5279d460.js";const v=p=>(H("data-v-4dc1372c"),p=p(),J(),p),le={class:"row q-pt-md q-ml-lg"},te={class:"col-1 comp-size"},se=v(()=>n("p",{style:{color:"#123499"},class:"text-bold"},"From Date",-1)),ae={class:"col-1 comp-size"},ne=v(()=>n("p",{style:{color:"#123499"},class:"text-bold"},"To Date",-1)),me={class:"col-1 comp-size"},ie=v(()=>n("p",{style:{color:"#123499"},class:"text-bold"},"Commission Level",-1)),re={class:"col-1 comp-size"},ue=v(()=>n("p",{style:{color:"#123499"},class:"text-bold"},"Paid Status",-1)),_e={class:"col-1 q-ml-lg q-mt-lg"},de={class:"q-ml-md q-mt-sm q-mr-lg q-pa-md"},ce={class:"row justify-start items-center"},ve=v(()=>n("span",{class:"q-ml-sm"},null,-1)),pe={__name:"CommissionsReportsPage",setup(p){const Q=Z(),_=a(null),d=a(null),f=a("All"),b=a("All"),I=a(["All","Paid","Yet to be paid","Issue with payments"]),U=a(["All","One","Two","Three","Four"]),h=a(""),g=a(!1),c=a(!1),A=a([]),L=a([{name:"customerNumber",required:!0,label:"Customer ID",align:"left",field:s=>s.customer_number,format:s=>`${s}`,sortable:!0},{name:"customerName",label:"Customer Name",field:"customer_name",sortable:!0,align:"left"},{name:"mobileNumber",label:"Mobile Number",field:"mobile_number",sortable:!0,align:"left"},{name:"bankName",label:"Bank Name",field:"name_of_bank",align:"left"},{name:"accountNumber",label:"Account Number",field:"account_number",align:"left"},{name:"ifscCode",label:"IFSC Code",field:"ifsc_code",align:"left"},{name:"pan",label:"PAN",field:"pan",align:"left"},{name:"plan",label:"Plan",field:"plan",align:"left"},{name:"registrationFee",label:"Registration Fee (Rs.)",field:"registration_fee",align:"center"},{name:"commissionFromDate",label:"Commission From Date",field:"commission_from_date",sortable:!0,align:"left"},{name:"commissionToDate",label:"Commission To Date",field:"commission_to_date",sortable:!0,align:"left"},{name:"levelOneCompletionStatus",label:"Completion (1st)",field:"level_one_completion_status",align:"center"},{name:"levelOneCompletionDate",label:"Completion Date (1st)",field:"level_one_completion_date",align:"left"},{name:"levelOneCommissionAmount",label:"Commission Amount (1st) (Rs.)",field:"level_one_commission_amount",align:"center"},{name:"levelOneTdsAmount",label:"TDS Amount (1st) (10%) (Rs.)",field:"level_one_tds_amount",align:"center"},{name:"levelOneAmountPayable",label:"Amount Payable (1st) (Rs.)",field:"level_one_amount_payable",align:"center"},{name:"levelOneCommissionPaidStatus",label:"Commission Payment (1st)",field:"level_one_commission_paid_status",sortable:!0,align:"center"},{name:"levelOneCommisionPaidDate",label:"Commission Paid Date (1st)",field:"level_one_commission_paid_date",sortable:!0,align:"center"},{name:"levelOneCommissionPaymentComments",label:"Commission Payment Comments (1st)",field:"level_one_payment_comments",align:"center"},{name:"levelTwoCompletionStatus",label:"Completion (2nd)",field:"level_two_completion_status",align:"center"},{name:"levelTwoCompletionDate",label:"Completion Date (2nd)",field:"level_two_completion_date",align:"left"},{name:"levelTwoCommissionAmount",label:"Commission Amount (2nd) (Rs.)",field:"level_two_commission_amount",align:"center"},{name:"levelTwoTdsAmount",label:"TDS Amount (2nd) (10%) (Rs.)",field:"level_two_tds_amount",align:"center"},{name:"levelTwoAmountPayable",label:"Amount Payable (2nd) (Rs.)",field:"level_two_amount_payable",align:"center"},{name:"levelTwoCommissionPaidStatus",label:"Commission Payment (2nd)",field:"level_two_commission_paid_status",sortable:!0,align:"center"},{name:"levelTwoCommisionPaidDate",label:"Commission Paid Date (2nd)",field:"level_two_commission_paid_date",sortable:!0,align:"center"},{name:"levelTwoCommissionPaymentComments",label:"Commission Payment Comments (2nd)",field:"level_two_payment_comments",align:"left"},{name:"levelThreeCompletionStatus",label:"Completion (3rd)",field:"level_three_completion_status",align:"center"},{name:"levelThreeCompletionDate",label:"Completion Date (3rd)",field:"level_three_completion_date",align:"center"},{name:"levelThreeCommissionAmount",label:"Commission Amount (3rd) (Rs.)",field:"level_three_commission_amount",align:"center"},{name:"levelThreeTdsAmount",label:"TDS Amount (3rd) (10%) (Rs.)",field:"level_three_tds_amount",align:"center"},{name:"levelThreeAmountPayable",label:"Amount Payable (3rd) (Rs.)",field:"level_three_amount_payable",align:"center"},{name:"levelThreeCommissionPaidStatus",label:"Commission Payment (3rd)",field:"level_three_commission_paid_status",sortable:!0,align:"center"},{name:"levelThreeCommisionPaidDate",label:"Commission Paid Date (3rd)",field:"level_three_commission_paid_date",sortable:!0,align:"center"},{name:"levelThreeCommissionPaymentComments",label:"Commission Payment Comments (3rd)",field:"level_three_payment_comments",align:"left"},{name:"levelFourCompletionStatus",label:"Completion (4th)",field:"level_four_completion_status",align:"center"},{name:"levelFourCompletionDate",label:"Completion Date (4th)",field:"level_four_completion_date",align:"center"},{name:"levelFourCommissionAmount",label:"Commission Amount (4th) (Rs.)",field:"level_four_commission_amount",align:"center"},{name:"levelFourTdsAmount",label:"TDS Amount (4th) (10%) (Rs.)",field:"level_four_tds_amount",align:"center"},{name:"levelFourAmountPayable",label:"Amount Payable (4th) (Rs.)",field:"level_four_amount_payable",align:"center"},{name:"levelFourCommissionPaidStatus",label:"Commission Payment (4th)",field:"level_four_commission_paid_status",sortable:!0,align:"center"},{name:"levelFourCommisionPaidDate",label:"Commission Paid Date (4th)",field:"level_four_commission_paid_date",sortable:!0,align:"center"},{name:"levelFourCommissionPaymentComments",label:"Commission Payment Comments (4th)",field:"level_four_payment_comments",align:"left"},{name:"userStatus",label:"User Status",field:"user_status",align:"center"}]),y=a([]),P=a(["customerNumber","customerName","levelOneCompletionStatus","levelOneCommissionPaidStatus","levelTwoCompletionStatus","levelTwoCommissionPaidStatus","levelThreeCompletionStatus","levelThreeCommissionPaidStatus","levelFourCompletionStatus","levelFourCommissionPaidStatus","userStatus"]),C=W(),B=j(()=>!_.value||!d.value),F=()=>{C.loading.show({spinner:X,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},q=()=>{C.loading.hide()},$=s=>{c.value=!1,s===!0&&(A.value=[],V())},w=s=>s=="Paid"?"green":s=="Payment Issue"?"brown":"red",V=()=>{if(d.value<_.value){C.notify({message:"Commission From Date should be less than or equal to Commission To Date!!!",type:"warning",position:"top"});return}F();let s={commission_from_date:_.value,commission_to_date:d.value,commission_status:f.value,commission_level:b.value};Q.getCommissionDetails(s).then(t=>{y.value=t.data.commissions}).catch(t=>{console.log("err",t)}).finally(()=>{q()})},E=()=>{F();let s=`Commissions_level_${b.value}_${f.value}_payment_status_${_.value}_to_${d.value}.xlsx`,t=[];for(let e of y.value){let M={"Customer Id":e.customer_number,"Customer Name":e.customer_name,"Mobile Number":e.mobile_number,"Bank Name":e.name_of_bank,"Account Number":e.account_number,"IFSC Code":e.ifsc_code,Pan:e.pan,Plan:e.plan,"Registration Fee (Rs.)":e.registration_fee,"Commission From Date":e.commission_from_date,"Commission To Date":e.commission_to_date,"Level One Completion Status":e.level_one_completion_status,"Level One Completion Date":e.level_one_completion_date,"Level One Commission Amount":e.level_one_commission_amount,"Level One TDS Amount (10%)":e.level_one_tds_amount,"Level One Amount Payable":e.level_one_amount_payable,"Level One Commssion Payment Status":e.level_one_commission_paid_status,"Level One Commission Paid Date":e.level_one_commission_paid_date,"Level One Commission Payment Comments":e.level_one_payment_comments,"Level Two Completion Status":e.level_two_completion_status,"Level Two Completion Date":e.level_two_completion_date,"Level Two Commission Amount":e.level_two_commission_amount,"Level Two TDS Amount (10%)":e.level_two_tds_amount,"Level Two Amount Payable":e.level_two_amount_payable,"Level Two Commssion Payment Status":e.level_two_commission_paid_status,"Level Two Commission Paid Date":e.level_two_commission_paid_date,"Level Two Commission Payment Comments":e.level_two_payment_comments,"Level Three Completion Status":e.level_three_completion_status,"Level Three Completion Date":e.level_three_completion_date,"Level Three Commission Amount":e.level_three_commission_amount,"Level Three TDS Amount (10%)":e.level_three_tds_amount,"Level Three Amount Payable":e.level_three_amount_payable,"Level Three Commssion Payment Status":e.level_three_commission_paid_status,"Level Three Commission Paid Date":e.level_three_commission_paid_date,"Level Three Commission Payment Comments":e.level_three_payment_comments,"Level Four Completion Status":e.level_four_completion_status,"Level Four Completion Date":e.level_four_completion_date,"Level Four Commission Amount":e.level_four_commission_amount,"Level Four TDS Amount (10%)":e.level_four_tds_amount,"Level Four Amount Payable":e.level_four_amount_payable,"Level Four Commssion Payment Status":e.level_four_commission_paid_status,"Level Four Commission Paid Date":e.level_four_commission_paid_date,"Level Four Commission Payment Comments":e.level_four_payment_comments};t.push(M)}ee(t,s),q()};return(s,t)=>(T(),Y(G,null,[n("div",le,[n("div",te,[se,l(S,{modelValue:_.value,"onUpdate:modelValue":t[0]||(t[0]=e=>_.value=e),style:{"max-width":"150px"},outlined:"",dense:"",autofocus:"",type:"date"},null,8,["modelValue"])]),n("div",ae,[ne,l(S,{modelValue:d.value,"onUpdate:modelValue":t[1]||(t[1]=e=>d.value=e),style:{"max-width":"150px"},outlined:"",dense:"",autofocus:"",type:"date"},null,8,["modelValue"])]),n("div",me,[ie,l(x,{filled:"",dense:"",style:{width:"150px"},modelValue:b.value,"onUpdate:modelValue":t[2]||(t[2]=e=>b.value=e),options:U.value},null,8,["modelValue","options"])]),n("div",re,[ue,l(x,{filled:"",dense:"",style:{width:"200px"},modelValue:f.value,"onUpdate:modelValue":t[3]||(t[3]=e=>f.value=e),options:I.value},null,8,["modelValue","options"])]),n("div",_e,[l(D,{unelevated:"",color:"primary",label:"Search","no-caps":"",disable:O(B),onClick:V},null,8,["disable"])])]),n("div",de,[l(D,{color:"green",class:"q-mb-md",style:{width:"20px"},"no-caps":"",onClick:E},{default:o(()=>[n("div",ce,[l(k,{name:"fas fa-file-excel"}),ve])]),_:1}),l(K,{class:"commissions-table",flat:"",bordered:"",title:"Commissions",rows:y.value,columns:L.value,"row-key":"customer_number",filter:h.value,"visible-columns":P.value},{"top-right":o(()=>[g.value?(T(),N(S,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:h.value,"onUpdate:modelValue":t[4]||(t[4]=e=>h.value=e),placeholder:"Search"},{append:o(()=>[l(k,{name:"search"})]),_:1},8,["modelValue"])):R("",!0),l(D,{class:"q-ml-sm q-mr-sm",icon:"filter_list",onClick:t[5]||(t[5]=e=>g.value=!g.value),flat:""}),l(x,{modelValue:P.value,"onUpdate:modelValue":t[6]||(t[6]=e=>P.value=e),multiple:"",outlined:"",dense:"","options-dense":"","display-value":O(C).lang.table.columns,"emit-value":"","map-options":"",options:L.value,"option-value":"name","options-cover":"",style:{"min-width":"150px"}},null,8,["modelValue","display-value","options"])]),"body-cell-userStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:e.row.user_status==="Active"?"green":"orange","text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.user_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelOneCompletionStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:e.row.level_one_completion_status==="Completed"?"green":"orange","text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_one_completion_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelTwoCompletionStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:e.row.level_two_completion_status==="Completed"?"green":"orange","text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_two_completion_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelThreeCompletionStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:e.row.level_three_completion_status==="Completed"?"green":"orange","text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_three_completion_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelFourCompletionStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:e.row.level_four_completion_status==="Completed"?"green":"orange","text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_four_completion_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelOneCommissionPaidStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:w(e.row.level_one_commission_paid_status),"text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_one_commission_paid_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelTwoCommissionPaidStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:w(e.row.level_two_commission_paid_status),"text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_two_commission_paid_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelThreeCommissionPaidStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:w(e.row.level_three_commission_paid_status),"text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_three_commission_paid_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),"body-cell-levelFourCommissionPaidStatus":o(e=>[l(u,{props:e},{default:o(()=>[l(r,{color:w(e.row.level_four_commission_paid_status),"text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:o(()=>[m(i(e.row.level_four_commission_paid_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),_:1},8,["rows","columns","filter","visible-columns"])]),c.value?(T(),N(oe,{key:0,modelValue:c.value,"onUpdate:modelValue":t[7]||(t[7]=e=>c.value=e),"show-edit-commission-popup":c.value,"close-edit-commission-popup":$,"selected-data":A.value},null,8,["modelValue","show-edit-commission-popup","selected-data"])):R("",!0)],64))}};var Ne=z(pe,[["__scopeId","data-v-4dc1372c"]]);export{Ne as default};
