<?

error_reporting(E_ALL);
set_time_limit(0); 
ini_set('memory_limit','-1');

require_once('inc/connection.php');
global $db;
$_TOTAL = $_TOTAL_FILES =  0;

function convertCSVtoDBX($sourceDest,$tableCoulmns,$sourceCoulmns,$dir,$delimeter,$dumpSeed=150)
{
     global $db,$_TOTAL, $_TOTAL_FILES;
     $sql_insert=$sql_insert1="";$row = $row_rr = 1;
     
     if(($handle_r = fopen($dir.$sourceDest[0],"r")) !== FALSE)
     {
	     $j = $jm = $i_mot = $NO_OF_COLUMNS = 0;
	     
	     while(!feof($handle_r))
	     {
		     $_data = str_getcsv(trim(fgets($handle_r)),$delimeter);
		     
		     if($row == 1)
		     {
			$NO_OF_COLUMNS = sizeof($_data);
			
			$sql_insert = "INSERT INTO `".$sourceDest[1]."` (";
			
			while(list($k,$v) = each($tableCoulmns))
			{
			   $sql_insert .= "`".str_replace(' ','_',$v)."`,";
			}
			
			$sql_insert .= "`571`,`572`,`573`,`date`) VALUES ";
		     }
		     
		     if($row < 2){$row++;continue;}
		     
		     $tempArr = $sourceCoulmns;
		     
		     if(true) // Place for Filtering Rules
		     {
			     if($i_mot==$dumpSeed)
			     {
				$sql_insert1 .= " (";
				
				while(list($k,$v) = each($tempArr))
				{
					$sql_insert1 .= $db->qstr(isset($_data[$v])?trim($_data[$v]):"").",";
				}
					
				$sql_insert1 .= $db->qstr($sourceDest[0]).",".$db->qstr($NO_OF_COLUMNS).",".$db->qstr($sourceDest[2]).",".$db->qstr(NOW()).");";
				@$db->Execute($sql_insert.$sql_insert1);
				
				$sql_insert1="";
				$i_mot=0;
			     }
			     else
			     {
				$sql_insert1 .= " (";
				
				while(list($k,$v) = each($tempArr))
				{
					$sql_insert1 .= $db->qstr(isset($_data[$v])?trim($_data[$v]):"").",";
				}
				
				$sql_insert1 .= $db->qstr($sourceDest[0]).",".$db->qstr($NO_OF_COLUMNS).",".$db->qstr($sourceDest[2]).",".$db->qstr(NOW())."),";
				
				$i_mot++;
			     }
		     }
		     
		     $row++;
	     }
	     
	     if(($i_mot>0) && ($i_mot<$dumpSeed)) // --- Dump last batch less than dumpSeed value
	     {
		     $sql_insert1 = substr($sql_insert1,0,-1).";";
		     @$db->Execute($sql_insert.$sql_insert1);
		     $sql_insert1="";$i_mot=0;
	     }
	     
	     if($row>2)
	     {
		echo "<table><tr>
		<td class='txtn2'  style='height:14px;text-align:left;color:green;font-size:12px;border-bottom:1px solid #ccc;' > Rows = <span style='color:#DB0000;'>".$row."</span></td><td class='txtn2'  style='border-bottom:1px solid #ccc;text-align:left;color:green;font-size:12px;' colspan='3'>File <span style='color:#DB0000;'>[ ".$sourceDest[2]." ] (".$NO_OF_COLUMNS." ) ".$sourceDest[0]."</span> successfully processed</td></tr>
		</table>";
		$_TOTAL = $_TOTAL + $row;
		$_TOTAL_FILES++;
	     }
	     fclose($handle_r);
     }else
     {
	     echo "<tr><td></td><td class='txtn2'  style='text-align:left;color:#DB0000;font-size:12px;' colspan='3'>Error - Cannot Open the file ".$sourceDest[0]."..</td></tr>";
     }
}

// --- EXECUTE THE FUNCTION EXAMPLE

$row = $row_rr = 1; $col = 0; $_sd = "";$qoArr = $qrArr = array();$_qo = $_qr = $_qoT = $_qrT = 0;$sql_insert="";

$_file = array("");
$_fieldArr=$new_data=$_data_ro=$_data_rz=$new_data1=$_tmp_arr=array();
$auto = array();

$start = microtime(true); // Your script content here

// -------------- STEP 1: Open the File ("filename.csv")

$dir = ROOTPATH."SYSTEM_FILES/MANUAL_UPLOADS/MASTER_DATA/";

$tableCoulmns = array("509","510",
		      "500","501","502","503","508","511","512","513","514",
		      "515","516","517",
		      
		      "523","524","525", "526","527","528", "529","530","531",
		      "534","535","536","537","538","539",
		      "540","541","542","543","544","545","546","547","548",
		      
			"549","550","551","552","553","554","555","562","563","564","565","566","567","568","569","570",
			"577","578","579","580","581","582","583","584","585","586","587","588","589","590","591",
			"593","594","595","596","597","598","599","600","601","602","603",
			"605","606","607","608","609","610","611","612","613","614","615"
			
		      );
$sourceCoulmns = array(0,1,
		       2,3,4,5,6,7,8,9,10,
		       11,12,13,
		       14,15,16,  17,18,19, 20,21,22,
		       23,24,25,26,27,28,
		       29,30,31,32,33,34,35,36,37,
		       
		       38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,
		       54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,
		       69,70,71,72,73,74,75,76,77,78,79,
		       80,81,82,83,84,85,86,87,88,89,90
		       );

$_display_results="";$arr= array();
if($handle = opendir ($dir)) 
{
  $_folder_index = 0;
  while(false !== ($file = readdir($handle))) 
  {
	if($file == ".DS_Store") continue;
	$nextpath = $dir . '/' . $file . '/CSV' ;$nextpath_ = $dir . $file . '/CSV' ; 
	
	if ($file != '.' && $file != '..' && !is_link ($nextpath)  && $file[0] != '.' && $file[0] != '..') 
	{
		if(is_dir ($nextpath))
		{
			$dir_ = $nextpath_."/"; //ROOTPATH."SYSTEM_FILES/MANUAL_UPLOADS/MASTER_DATA/";
			if($handle_ = opendir ($nextpath_)) 
			{
				$_file_index = 0;
				while(false !== ($file_ = readdir($handle_)))
				{
					if($file_ == ".DS_Store") continue;
					$nextpath__ = $nextpath_ . '/' . $file_;
					
					if ($file_ != '.' && $file_ != '..' && !is_link ($nextpath__)  && $file_[0] != '.' && $file_[0] != '..')
					{
						if(!is_dir ($nextpath__))
						{
							$_file_index++;
							$sourceDest = array($file_,"_mod_63",$file);
							convertCSVtoDBX($sourceDest,$tableCoulmns,$sourceCoulmns,$dir_,";",1,false);
						}
					}
				}
			}
		}
	}
  } 
} 
closedir ($handle);

$end = microtime(true);

$time = number_format(($end - $start), 2);// echo 'This page loaded in ', $time, ' seconds';

$_BODY =  "<table padding=5>";
$_BODY .=  "<tr><td style='height:25px;padding:10px;font-size:14px;background-color:#b8dafd;'>Number of Files</td>
<td style='height:25px;padding:10px;font-size:14px;background-color:#c2e5ca;'>Total No. of Records Processed</td>
<td style='height:25px;padding:10px;font-size:14px;background-color:#f5c6cb;'>Total Time Elapsed</td></tr>";

$_BODY .="<tr><td style='height:25px;padding:10px;font-size:14px;font-weight:bold;'>".$_TOTAL_FILES."</td>
<td style='height:25px;padding:10px;font-size:14px;font-weight:bold;'>".$_TOTAL."</td>
<td style='height:25px;padding:10px;font-size:14px;font-weight:bold;'>".$time." seconds</td></tr>
";

$_BODY .= "</table>";

echo $_BODY;

?>
