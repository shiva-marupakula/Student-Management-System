<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>
<%
String course=request.getParameter("course");
String branch=request.getParameter("branch");
String rollNo=request.getParameter("rollNo");
String name=request.getParameter("name");
String fatherName=request.getParameter("fatherName");
String gender=request.getParameter("gender");
String password=request.getParameter("password");

try
{
	Connection con=ConnectionProvider.getCon();
	Statement st=con.createStatement();
	st.executeUpdate("insert into student values('"+course+"','"+branch+"','"+rollNo+"','"+name+"','"+fatherName+"','"+gender+"','"+password+"')");
	response.sendRedirect("adminHome.jsp");
	/*int i = st.executeUpdate();
	if(i > 0)
	{
		out.print("Record Updated Successfully");
	}
	else
	{
			out.print("There is a problem in updating Record.");
	}*/
	
}
catch(Exception e)
{
	out.println(e);
}
%>
