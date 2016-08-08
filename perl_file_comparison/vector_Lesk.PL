use WordNet::QueryData;
use WordNet::Similarity::path;
use WordNet::Similarity::lch;
use WordNet::Similarity::res;
use WordNet::Similarity::jcn;
use WordNet::Similarity::lin;
use WordNet::Similarity::wup;
use WordNet::Similarity::lesk;
use WordNet::Similarity::hso;
use WordNet::Similarity::random;
use WordNet::Similarity::ICFinder;
use WordNet::Similarity::PathFinder;

sub calaculaterelatedness
{
	my $measure = WordNet::Similarity::path->new ($wn);
	my $measure_type = @_[0];
	my $w1 = @_[1];
	my $w2 = @_[2];
	my $wn = WordNet::QueryData->new;
	if ($measure_type==0)
	{
		$measure = WordNet::Similarity::path->new ($wn);
	}
	if ($measure_type==1)
	{
		$measure = WordNet::Similarity::lch->new($wn);
                $threshold = 1.5;
	}
	if ($measure_type==2)
	{
		$measure = WordNet::Similarity::res->new($wn);
                $threshold = 5;
	}
	if ($measure_type==3)
	{
		$measure = WordNet::Similarity::jcn->new($wn);
                $threshold = 0.04;
	}
	if ($measure_type==4)
	{
		$measure = WordNet::Similarity::wup->new($wn);
	}
	if ($measure_type==5)
	{
		$measure = WordNet::Similarity::lin->new($wn);
                $threshold = 0.1;
	}
	if ($measure_type==6)
	{
		$measure = WordNet::Similarity::lesk->new($wn);
                $threshold = 0.1;
	}


	open(MYINPUTFILE, "<$w1"); # open for input
	open(MYINPUTFILE2, "<$w2"); # open for input
	my(@lines) = <MYINPUTFILE>; # read file into list
	my(@lines2) = <MYINPUTFILE2>; # read file into list
	my($line);
	my($line2);

	# preparing file for output
	# recorded in report.txt
	my $filename = 'report.txt';
	open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

	# clear extra spacing at ends of words in file 1
	foreach $line (@lines)
	{
		$line =~ s/^\s+|\s+$//g;

	}

	# clear extra spacing at ends of words in file 1
	foreach $line2 (@lines2)
	{
		$line2 =~ s/^\s+|\s+$//g;

	}

	#my @array = ();
	#foreach my $i ( 0 .. scalar @lines ) {
  	#	foreach my $j ( 0 .. (scalar @lines2)) {
	#		my $value = $measure->getRelatedness("$lines[$i]#n#1", "$lines2[$j]#v#1");
	#		push @{ $array[$i] }, $value;
  	#	}
	#}


	print $fh "motions : ";
	foreach $line2 (@lines2) # loop thru list 2
		{
		print $fh "$line2 "; # output first word, second word, value
		}
	print $fh " \n";
	print $fh " \n";


	my @array = ();
	foreach my $i ( 0 .. (scalar @lines) - 1 ) {
		print $fh "O$i : ";
  		foreach my $j ( 0 .. (scalar @lines2) - 1) {
			my $value = $measure->getRelatedness("$lines[$i]#n#1", "$lines2[$j]#v#1");
    			push @{ $array[$i] }, $value;
			#print $fh "$array[$i][$j] ";
			print $fh "$value ";
  		}
		print $fh "\n";
	}



	#print $fh "$array[3][2]";

	#my($z) = 0;
	#foreach $line (@lines) # loop thru list 1
 	#{
	#	print $fh "O$z :";
 	#	foreach $line2 (@lines2) # loop thru list 2
	#	{
	#	my $value = $measure->getRelatedness("$line#n#1", "$line2#v#1"); # calculate relatedness between the two words
	#	print $fh "$value "; # output first word, second word, value
	#	}
	#	$z = $z + 1;
	#	print $fh "\n";
 	#}


	close $fh;
	print "done\n";
}


print "Calculating Relatedness .... \n";
calaculaterelatedness(6,'objects.txt','motions.txt');
