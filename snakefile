rule all:
	input:
		'emis_box.png', 'emis_hist.png', 'upop_emis_corr.png'

rule dwnld_data:
	output:
		'Agrofood_co2_emission.csv'
	shell:
		'wget -O {output} "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'

rule plot_box:
    input:
        'Agrofood_co2_emission.csv'
    params:
        cc = 0,
        c = 'Albania',
        ec = 29,
        xl = 'Emissions',
        yl = 'Amount'
    output:
        'emis_box.png' #{x} is a wild card {} are variables AND wildcards
    shell:
        'python src/box.py --filename {input}  --country {params.c}  --country_column {params.cc}  --emissions_column {params.ec} --xlabel {params.xl} --ylabel {params.yl}  --output_nm {output}'

rule plot_hist:
        input:
                'Agrofood_co2_emission.csv'
        params:
            cc = 0,
            c = 'Albania',
            ec = 29,
            xl = 'Emissions',
            yl = 'Amount_of_Emissions'
        output:
                'emis_hist.png' #{x} is a wild card {} are variables AND wildcards
        shell:
                'python src/hist.py --filename {input}  --country {params.c}  --country_column {params.cc}  --emissions_column {params.ec} --xlabel {params.xl} --ylabel {params.yl}  --output_nm {output}'

rule plot_corr:
    input:
        'Agrofood_co2_emission.csv'
    params:
        cc = 0,
        c = 'Albania',
        ec = 29,
        uc = 26,
        xl = 'Urban_Population',
        yl = 'Emissions'
    output:
        'upop_emis_corr.png' #{x} is a wild card {} are variables AND wildcards
    shell:
        'python src/correlation.py --filename {input}  --country {params.c}  --urban_column {params.uc} --country_column {params.cc}  --emissions_column {params.ec} --xlabel {params.xl} --ylabel {params.yl}  --output_nm {output}'
