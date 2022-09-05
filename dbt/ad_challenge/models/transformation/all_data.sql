{{ config(materialized='table') }}

select
    briefing.campaign_id,
    briefing.campaign_name,
    briefing.submission_date,
    briefing.description,
    briefing.campaign_objectives,
    briefing.kpis,
    briefing.placements,
    briefing.start_date,
    briefing.end_date,
    briefing.serving_locations,
    briefing.black_white_audience_list_included,
    briefing.delivery_requirements,
    briefing.cost_centre,
    briefing.currency,
    briefing.buy_rate,
    briefing.volume_agreed,
    briefing.gross_cost,
    briefing.agency_fee,
    briefing.percentage,
    briefing.flat_fee,
    briefing.net_cost,
    campains_table.type,
    campains_table.width,
    campains_table.height,
    campains_table.creative_id,
    campains_table.auction_id,
    campains_table.browser_ts,
    campains_table.game_key,
    campains_table.geo_country,
    campains_table.site_name,
    campains_table.platform_os,
    campains_table.device_type,
    campains_table.browser,
    global_design.labels,
    global_design.text,
    global_design.colors,
    global_design.video_data,
    global_design.eng_type,
    global_design.direction,
    global_design.adunit_size_X


from (({{ ref('briefing') }}
    full outer join {{ ref('campains_table') }}
    ON briefing.campaign_id = campains_table.campaign_id)
    full outer join {{ ref('global_design') }}
    ON global_design.game_key = campains_table.game_key)