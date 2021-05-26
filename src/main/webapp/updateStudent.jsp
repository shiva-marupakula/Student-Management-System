<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>
<%String course= request.getParameter("course");
String branch=request.getParameter("branch");
String rollNo=request.getParameter("rollNo");
String name=request.getParameter("name");
String fatherName=request.getParameter("fatherName");
String gender=request.getParameter("gender");
String password=request.getParameter("password");
if(rollNo != null)
{
Connection con = null;
PreparedStatement ps = null;
int personID = Integer.parseInt(rollNo);
try
{
Class.forName("com.mysql.jdbc.Driver");
con = DriverManager.getConnection("jdbc:mysql://localhost:3306/project","root","root");
String sql="Update student set course=?,branch=?,name=?,fatherName=?,gender=?,password=? where rollNo="+rollNo;
response.sendRedirect("adminHome.jsp");
ps = con.prepareStatement(sql);
ps.setString(1,course);
ps.setString(2, branch);
ps.setString(3, name);
ps.setString(4, fatherName);
ps.setString(5, gender);
ps.setString(6, password);
int i = ps.executeUpdate();
if(i > 0)
{
	out.print("Record Updated Successfully");
}
else
{
		out.print("There is a problem in updating Record.");
}
}
catch(Exception e)
{
	
}
}
%>