<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>
<% 
String rollNo=request.getParameter("rollNo");
//session.putValue("userid",userid);
String password=request.getParameter("password");
Connection con=ConnectionProvider.getCon();
Statement st=con.createStatement();
ResultSet rs=st.executeQuery("select * from student where rollNo='"+rollNo+"' and password='"+password+"'");
try{
rs.next();
if(rs.getString("password").equals(password)&&rs.getString("rollNo").equals(rollNo))
{
response.sendRedirect("studentLoginAction.jsp");
	out.println("Welcome " +rollNo);
}
else{
out.println("Invalid password or username.");
}
}
catch (Exception e) {
	out.println(e);
	e.printStackTrace();
}

%>