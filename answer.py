<html>
<head>
<title>result.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
result.py</font>
</center></td></tr></table>
<pre><span class="s0">math = int(input(</span><span class="s1">&quot;enter math marks : &quot;</span><span class="s0">))</span>
<span class="s0">science = int(input(</span><span class="s1">&quot;enter science marks : &quot;</span><span class="s0">))</span>
<span class="s0">social = int(input(</span><span class="s1">&quot;enter social marks : &quot;</span><span class="s0">))</span>
<span class="s0">english = int(input(</span><span class="s1">&quot;enter english marks : &quot;</span><span class="s0">))</span>
<span class="s0">hindi = int(input(</span><span class="s1">&quot;enter hindi marks : &quot;</span><span class="s0">))</span>
<span class="s0">kannada = int(input(</span><span class="s1">&quot;enter kannada marks : &quot;</span><span class="s0">))</span>
<span class="s0">sum = math+science+social+english+hindi+kannada</span>
<span class="s0">print(</span><span class="s1">&quot;**********************&quot;</span><span class="s0">)</span>
<span class="s0">print(</span><span class="s1">&quot;total marks are : &quot;</span><span class="s2">,</span><span class="s0">sum)</span>
<span class="s0">per = (sum/</span><span class="s3">625</span><span class="s0">)*</span><span class="s3">100</span>
<span class="s0">print(</span><span class="s1">&quot;percentage is : &quot;</span><span class="s2">,</span><span class="s0">per)</span>
<span class="s0">print(</span><span class="s1">&quot;**********************&quot;</span><span class="s0">)</span>
<span class="s2">if </span><span class="s0">(math &gt;= </span><span class="s3">35 </span><span class="s2">and </span><span class="s0">science &gt;= </span><span class="s3">35 </span><span class="s2">and </span><span class="s0">social &gt;= </span><span class="s3">35 </span><span class="s2">and </span><span class="s0">english &gt;= </span><span class="s3">35 </span><span class="s2">and </span><span class="s0">hindi &gt;= </span><span class="s3">35 </span><span class="s2">and </span><span class="s0">kannada &gt;= </span><span class="s3">35</span><span class="s0">):</span>
  <span class="s0">res = print(</span><span class="s1">&quot;Pass&quot;</span><span class="s0">)</span>
  <span class="s2">if </span><span class="s0">(per &lt;= </span><span class="s3">100 </span><span class="s2">and </span><span class="s0">per &gt;= </span><span class="s3">85</span><span class="s0">):</span>
    <span class="s0">print(</span><span class="s1">&quot;distinction&quot;</span><span class="s0">)</span>
  <span class="s2">elif </span><span class="s0">(per &lt;= </span><span class="s3">85 </span><span class="s2">and </span><span class="s0">per &gt;= </span><span class="s3">60</span><span class="s0">):</span>
    <span class="s0">print(</span><span class="s1">&quot;1st class&quot;</span><span class="s0">)</span>
  <span class="s2">elif </span><span class="s0">(per &lt;= </span><span class="s3">60 </span><span class="s2">and </span><span class="s0">per &gt;= </span><span class="s3">50</span><span class="s0">):</span>
    <span class="s0">print(</span><span class="s1">&quot;2nd class&quot;</span><span class="s0">)</span>
  <span class="s2">elif </span><span class="s0">(per &lt;= </span><span class="s3">50 </span><span class="s2">and </span><span class="s0">per &gt;= </span><span class="s3">35</span><span class="s0">):</span>
    <span class="s0">print(</span><span class="s1">&quot;3rd class&quot;</span><span class="s0">)</span>
  <span class="s2">else </span><span class="s0">:</span>
    <span class="s0">print(</span><span class="s1">&quot;fail&quot;</span><span class="s0">)</span>
<span class="s2">else</span><span class="s0">:</span>
  <span class="s0">res = print(</span><span class="s1">&quot;final result fail&quot;</span><span class="s0">)</span></pre>
</body>
</html>