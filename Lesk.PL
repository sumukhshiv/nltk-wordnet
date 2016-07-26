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

sub eliminatespaces
{
	for ($i=0; $i<$num; $i++)
	{   
		$array[$i] =~ s/^\s+|\s+$//g;
	}
}

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

	my $value = $measure->getRelatedness("$w1#n#1", "$w2#n#1"); 
	my ($error, $errorString) = $measure->getError();
	die $errorString if $error;
	#print "$array[$i] (sense 1) <-> $array[$j] (sense 2) = $value\n";
}


print "Calculating Relatedness .... \n";
calaculaterelatedness(4,'book','cook');
